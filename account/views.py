from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from account.forms import NewUserRegisterForm
from .models import Account

class UserRegisterView(CreateView):
    template_name = 'account/register.html'
    form_class = NewUserRegisterForm
    success_url = reverse_lazy('account:user_login')

# login(request, form1, backend='django.contrib.auth.backends.ModelBackend')

class UserLoginView(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
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


def user_dashboard_page_view(request, username):
    template_name = 'account/dashboard.html'
    return render(request, template_name)
