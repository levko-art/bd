from django.urls import path
from .views import *


urlpatterns = [
    path('sign_in', sign_in, name='sign-in'),
    path('sign_up', sign_up, name='sign-up'),
]
