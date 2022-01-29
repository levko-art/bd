from django.http import FileResponse
from django_pandas.io import read_frame
from users.models import Counter, Transaction


def set_transaction_file(request):
    payments_frame = read_frame(
        Transaction.objects.filter(appointment=request.POST['appointment'], client=request.user)
    )
    payments_frame.to_csv(
        f'static/reports/{request.POST["appointment"]}/{request.user}.csv', 
        encoding='utf-8', 
        index=False
    )


def set_counter_file(request):
    payments_frame = read_frame(
        Counter.objects.filter(type=request.POST['appointment'], client=request.user)
    )
    payments_frame.to_csv(
        f'static/reports/{request.POST["appointment"]}/{request.user}.csv',
        encoding='utf-8',
        index=False
    )


def get_file(request):
    file_path = f'static/reports/{request.POST["appointment"]}/{request.user}.csv'
    return FileResponse(open(file_path, 'rb'))


def generate_report(request):
    set_transaction_file(request)
    return get_file(request)


def generate_counter_report(request):
    set_counter_file(request)
    return get_file(request)
