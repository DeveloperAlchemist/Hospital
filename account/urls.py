from django.urls import path
from account.views import *

urlpatterns = [
    path('sign-up/', sign_up),
    path('login/', login),
]