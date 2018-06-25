from django.shortcuts import render
from django.conf import settings
from .models import Product, Category, Cart
# Create your views here.

def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products, 'categorys': categorys}
    return render(request, 'main/index.html', context)

def checkout(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'main/checkout.html', context)

def contact(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'main/contact.html', context)

def product_details(request, productcode):
    products = Product.objects.filter(productcode = productcode)
    categorys = Category.objects.all()
    context = {'products':products, 'productcode':productcode,'categorys': categorys}
    return render(request, 'main/product_detail.html', context)

def products(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'main/products.html', context)

def cart(request):
	carts = Cart.objects.all()
	categorys = Category.objects.all()
	context = {'categorys': categorys, 'carts' : carts}
	return render(request, 'main/cart.html', context)

def register(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'main/register.html', context)

def search(request):
    quer = request.GET.get('quer', '')
    products = Product.objects.filter(title__icontains = quer)
    context = {'products':products}
    return render(request, 'main/search.html', context )