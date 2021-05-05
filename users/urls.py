from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('building_service/', building_service, name="building-service"),
    path('electricity/', electricity, name="electricity"),
    path('water/', water, name="water"),
    path('master_call/', master_call, name="master-call"),
    path('information/', information, name="information"),
    path('questionnaire/', questionnaire, name="questionnaire")
]
