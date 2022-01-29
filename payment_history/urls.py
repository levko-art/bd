from django.urls import path
from .views import generate_report, generate_counter_report


urlpatterns = [
    path('report/payments', generate_report, name='generate-report'),
    path('report/counters', generate_counter_report, name='generate-counter-report'),
]
