from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def bad_request(request, exception):
    context = {}
    return render(request, 'error_handling/400.html', context, status=400)


def permission_denied(request, exception):
    context = {}
    return render(request, 'error_handling/403.html', context, status=403)

def page_not_found(request, exception):
    print(exception)
    context = {}
    return render(request, 'error_handling/404.html', context, status=404)


def server_error(request):
    context = {}
    return render(request, 'error_handling/500.html', context, status=500)
