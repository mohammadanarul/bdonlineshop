from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.forms import user_register_form

def user_register_page(request):
    if request.method == 'POST':
        form = user_register_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')

def user_login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

def user_logout_page(request):
    logout(request)
    return redirect('/')

