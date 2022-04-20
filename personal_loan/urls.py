# from django import views
from multiprocessing.managers import Namespace
from xml.etree.ElementInclude import include
from django.urls import path
from personal_loan.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('create_loan/', loan_data.as_view()),
    
]
