from django.shortcuts import render, redirect
from account.forms import user_register_form

def user_register_page(request):
    form = user_register_form()
    if request.method == 'POST':
        form = user_register_form()
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'account/register.html', {'form': form})

