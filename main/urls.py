from django.urls import path
from main.views import *

urlpatterns = [
    path('get-information/', get_information),
    # path('get-child-info/', child_information),
]