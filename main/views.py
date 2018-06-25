from django.shortcuts import render
from django.conf import settings
<<<<<<< HEAD
from .models import Product, Category, Cart
=======
from .models import Product, Category
from .forms import UserForm
>>>>>>> 0e8581563a4da58d567bbeb2ef0602e6244234ff
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
<<<<<<< HEAD

# def search(request):
#     quer = request.GET.get('quer', '')
#     products = Product.objects.filter(title__icontains = quer)
#     context = {'products':products, 'quer':quer}
#     return render(request, 'main/index.html', context )

def search(request):
    if request.method == 'GET':
        book_name = request.GET['search']
        status = Product.objects.filter(title = book_name)
        return render(request, "main/index.html", {'items':status})
=======
>>>>>>> 0e8581563a4da58d567bbeb2ef0602e6244234ff
