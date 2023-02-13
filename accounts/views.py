from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return HttpResponse('products')


def customers(request):
    return HttpResponse('customers')
