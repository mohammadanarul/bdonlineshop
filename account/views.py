from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.forms import user_register_form

def user_register_page(request, *args, **kwargs):
    form = user_register_form()
    if request.method == 'POST':
        form = user_register_form(request.POST or None)
        if form.is_valid():
            form1 = form.save()
            login(request, form1, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('account:user_dashboard')
    else:
        form = user_register_form()
    template_name = 'account/register.html'
    return render(request, template_name, {'form': form})

def user_login_page(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    template_name = 'account/login.html'
    return render(request, template_name)

def user_logout_page(request):
    logout(request)
    return redirect('/')


def user_dashboard_page_view(request, username):
    template_name = 'account/dashboard.html'
    return render(request, template_name)
