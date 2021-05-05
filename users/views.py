from django.shortcuts import render


def dashboard(request):
    return render(request, 'users/dashboard.html', {})


def building_service(request):
    return render(request, 'users/building-service.html', {})


def electricity(request):
    return render(request, 'users/electricity.html', {})


def water(request):
    return render(request, 'users/water.html', {})


def master_call(request):
    return render(request, 'users/master-call.html', {})


def information(request):
    return render(request, 'users/information.html', {})


def questionnaire(request):
    return render(request, 'users/questionnaire.html', {})
