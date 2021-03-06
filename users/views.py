from django.shortcuts import render, redirect

from .models import Account, Client, Metric, Task, Transaction
from service.models import StaffPhone


def sign_up(request):
    return render(request, 'auth/sign_up.html', {})


def sign_in(request):
    return render(request, 'auth/sign_in.html', {})


def dashboard(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    return render(request, 'dashboard/dashboard.html', {'accounts': accounts})


def building_service(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    target_account = Account.objects.filter(client=request.user, is_active=True, type=0)[0]
    transactions = Transaction.objects.filter(client=request.user, appointment=0).order_by('-date')[:10]
    return render(
        request,
        'dashboard/building-service.html',
        {'accounts': accounts, 'target_account': target_account, 'transactions': transactions}
    )


def water(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    target_account = Account.objects.filter(client=request.user, is_active=True, type=1)[0]
    transactions = Transaction.objects.filter(client=request.user, appointment=1).order_by('-date')[:10][::-1]
    metrics = Metric.objects.filter(client=request.user, appointment=1).order_by('-date')[:10][::-1]
    return render(
        request,
        'dashboard/water.html',
        {'accounts': accounts, 'target_account': target_account, 'transactions': transactions, 'metrics': metrics}
    )


def electricity(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    target_account = Account.objects.filter(client=request.user, is_active=True, type=2)[0]
    transactions = Transaction.objects.filter(client=request.user, appointment=2).order_by('-date')[:10][::-1]
    metrics = Metric.objects.filter(client=request.user, appointment=2).order_by('-date')[:10][::-1]
    return render(
        request,
        'dashboard/electricity.html',
        {'accounts': accounts, 'target_account': target_account, 'transactions': transactions, 'metrics': metrics}
    )


def master_call(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    tasks = Task.objects.filter(client=request.user)
    user = request.user
    return render(request, 'dashboard/master-call.html', {'accounts': accounts, 'tasks': tasks, 'user': user})


def information(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    staff_phones = StaffPhone.objects.all()
    return render(request, 'dashboard/information.html', {'accounts': accounts, 'staff_phones': staff_phones})


def questionnaire(request):
    accounts = Account.objects.filter(client=request.user, is_active=True)
    client = Client.objects.get(username=request.user)
    return render(request, 'dashboard/questionnaire.html', {'accounts': accounts, 'client': client})


def update_questionnaire(request):
    username = request.POST['username']
    users = Client.objects.filter(username=username)
    if len(users) != 0:
        if users[0]:
            user = users[0]
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.reserve_phone = request.POST['reserve_phone']
            if request.POST['password'] != '':
                user.password = request.POST['password']
            user.save()

    return redirect("http://127.0.0.1:8000/")
