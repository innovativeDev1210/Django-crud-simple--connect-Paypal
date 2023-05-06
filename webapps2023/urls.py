from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('wallet/', include('wallet.urls')),
    path('transaction/', include('transaction.urls')),
    path('paypal/', include('payapp.urls')),
]
