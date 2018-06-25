from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Product, Category, Cart
from .forms import UserForm, CartForm
# Create your views here.

def index(request):
    submitbutton = request.POST.get('submit')
    string=""
    form=UserForm(request.POST or None)
    products = Product.objects.all()
    if form.is_valid():
        string=form.cleaned_data.get('searchStr')
        products = Product.objects.filter(title=string)

    categorys = Category.objects.all()
    context = {'form':form, 'string':string, 'submitbutton':submitbutton,'products':products, 'categorys': categorys}
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
	else:
		form = CartForm()

	context = {'products':products, 'productcode':productcode,'categorys': categorys, 'form': form}
	return render(request, 'main/product_detail.html', context)

def products(request, title):
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
