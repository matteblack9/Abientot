from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def contact(request):
    return render(request, 'main/contact.html')

def product_detail(request):
    return render(request, 'main/product_detail.html')

def products(request):
    return render(request, 'main/products.html')

def cart(request):
    return render(request, 'main/cart.html')

def register(request):
    return render(request, 'main/register.html')
