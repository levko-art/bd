from django.shortcuts import render


def login(request):
    return render(request, 'login/login.html', {})


def sign_in(request):
    return render(request, 'login/signin.html', {})
