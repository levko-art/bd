from django.urls import path
from .views import *


urlpatterns = [
    path('sign_in', sign_in, name='sign-in'),
    path('sign_up', sign_up, name='sign-up'),
    path('open_access', open_access, name='open-access'),
    path('forget_password', forget_password, name='forget-password'),
]
