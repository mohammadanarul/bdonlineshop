from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.http.response import BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from account.forms import AccountRegisterForm
from .models import Account

# authenticated
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from .tokens import UserAccountRegisterActiveTokenGenerate
from django.conf import settings
from orders.models import Order
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Q

class UserRegisterView(CreateView):
    template_name = 'account/register.html'
    form_class = AccountRegisterForm
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        email_template_name = 'account/email-confirm.html'
        message = render_to_string(email_template_name,{
            'user': instance,
            'domain': site.domain,
            'uid': instance.id,
            'token': UserAccountRegisterActiveTokenGenerate.make_token(instance)
        })
        to_mail = form.cleaned_data.get('email')
        to_list = [to_mail]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        # Success registration message
        messages.info(self.request, 'Check Your Email For Account Activation Link.')
        return super(UserRegisterView, self).form_valid(form)

class UserAccountActivateView(View):
    def get(self, request, uid, token, *args, **kwargs):
        try:
            user = get_object_or_404(Account, pk=uid)
        except:
            raise Http404('User is not valide')

        if user is not None and UserAccountRegisterActiveTokenGenerate.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'account/active-redirect.html')
        else:
            return render(request, 'account/activate-invalid.html')

class PasswordResetView(View):
    template_name="password_reset/password_reset.html"
    def get(self, request, *args, **kwargs):
        password_reset_form = PasswordResetForm()
        context={"password_reset_form":password_reset_form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = Account.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "password_reset/password_reset_email.html"
                        site = get_current_site(request)
                        c = {
                            "email":user.email,
                            'domain': site.domain, 
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        from_email = settings.EMAIL_HOST_USER
                        try:
                            send_mail(subject, email, from_email , [user.email], fail_silently=False)
                            return redirect('/')
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                            return redirect ("/password_reset/done/")
# login(request, form1, backend='django.contrib.auth.backends.ModelBackend')
    
class UserLoginView(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

class UserLogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('/')


class DashboardView(LoginRequiredMixin, View):
    template_name = 'account/dashboard.html'
    def get(self, request, username, *args, **kwargs):
        account = Account.objects.get(username=username)
        orders = Order.objects.get(user=request.user, ordered=True)
        return render(request, self.template_name, {'account':account, 'orders':orders})
