from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Product, Category, Cart
<<<<<<< HEAD
from django.conf import settings
from .forms import UserForm,CartForm
=======
from .forms import UserForm, CartForm
# Create your views here.
>>>>>>> fa756152f38d7d2656ea2043afe327ecf194e5c1

def index(request):
    buyertype = request.POST.get('buyer_')
    sellertype = request.POST.get('seller_')
    
    usertype = 3
    if sellertype:
        usertype = 2
    check_ = 2

    submitbutton = request.POST.get('submit')
    string=""
    form=UserForm(request.POST or None)
    products = Product.objects.all()
    if form.is_valid():
        string=form.cleaned_data.get('searchStr')
        products = Product.objects.filter(title__iexact=string)

    categorys = Category.objects.all()
    context = {'form':form, 'string':string, 'submitbutton':submitbutton,
    'products':products, 'categorys': categorys, 'type' : usertype, 'check_' : check_}
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
	product = get_object_or_404(Product, pk=productcode)
	categorys = Category.objects.all()
	if request.method == "POST":
		form = CartForm(request.POST)

		tmp = Cart.objects.filter(product = product)
		if form.is_valid():
			cart = form.save(commit=False)
			cart.product = product
			cart.total = int(cart.product.price) * int(cart.quantity)
			if(len(tmp) == 0) :
				cart.save()
			else :
				tmp[0].total =  int(cart.total) + int(tmp[0].total)
				tmp[0].quantity = int(cart.quantity) + int(tmp[0].quantity)
				tmp[0].save()
			context = {'products':products, 'productcode':productcode,'categorys': categorys, 'form': form}
			return redirect('cart')

	else:
		form = CartForm()

	context = {'products':products, 'productcode':productcode,'categorys': categorys, 'form': form}
	return render(request, 'main/product_detail.html', context)
<<<<<<< HEAD
	
def products(request):
=======

def products(request, title):
>>>>>>> fa756152f38d7d2656ea2043afe327ecf194e5c1
    categorys = Category.objects.all()
    category = Category.objects.get(title=title)
    products = Product.objects.filter(category=category)
    context = {'categorys':categorys, 'products':products}
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
