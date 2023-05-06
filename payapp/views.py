from django.shortcuts import render, redirect

def paypal(request):
    return render(request, 'paypal.html', {})