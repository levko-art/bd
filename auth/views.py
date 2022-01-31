from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from bd_service import settings
from users.models import Client


def sign_up(request):
    return render(request, 'auth/sign_up.html', {})


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    users = Client.objects.filter(username=username, password=password)
    if len(users) != 0:
        if users[0]:
            authenticate(username=username, password=password)
            login(request, users[0])
            return HttpResponseRedirect(reverse(settings.SUCCESS_SIGN_IN_REDIRECT_URL))
    else:
        return redirect("http://127.0.0.1:8000/sign_up")


def open_access(request):
    username = request.POST['username']
    users = Client.objects.filter(username=username)
    if len(users) != 0:
        if users[0]:
            user = users[0]
            if user.phone == request.POST['phone']:
                user.password = request.POST['password']
                user.save()
    return redirect("http://127.0.0.1:8000/")


def forget_password(request):
    username = request.POST['username']
    users = Client.objects.filter(username=username)
    if len(users) != 0:
        if users[0]:
            user = users[0]
            send_mail('Нагадування паролю', f'Ваш пароль {user.password}', None, [f'{user.email}'])
    return redirect("http://127.0.0.1:8000/")
