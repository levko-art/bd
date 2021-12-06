from django.urls import path
from .views import *


urlpatterns = [
    path('', login, name="login"),
    path('sign_in', sign_in, name="sign_in"),
]
