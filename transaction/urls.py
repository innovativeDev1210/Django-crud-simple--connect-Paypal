from django.urls import path
from . import views

# app_name = 'wallet'

urlpatterns = [
    path('', views.home, name="transaction"),
    path('request/<int:id>', views.request, name="request"),
    path('accept/<int:id>', views.accept, name="accept"),
    path('reject/<int:id>', views.reject, name="reject"),
    path('re_req/<int:id>', views.re_req, name="re_req"),
]