from django.contrib.auth import authenticate, login
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
    user = Client.objects.filter(username=username, password=password)[0]
    if user:
        authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse(settings.SUCCESS_SIGN_IN_REDIRECT_URL))
    else:
        return redirect("http://127.0.0.1:8000/sign_up")
