from django.urls import path
from . import views

# app_name = 'wallet'

urlpatterns = [
    path('', views.home, name="my_wallet"),
    path('form/', views.form, name="form"),
    path('transfer/', views.transfer, name="transfer"),
    path('change/<str:id>', views.change, name="change"),
]