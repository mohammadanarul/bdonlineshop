from django.shortcuts import render


def HomeView(request):
    template_name = 'shop/home.html'
    return render(request, template_name)
