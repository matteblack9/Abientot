from django.shortcuts import render
from django.conf import settings
from .models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main/index.html', context)

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

def search(request):
    products = Product.objects.all()
    quer = request.GET.get('quer','')
    products = products.filter(title__icontains = quer)
    context = {'products' : products}
    return render(request, 'main/cart.html', context)
