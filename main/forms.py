from django import forms
from .models import Cart, Product

class UserForm(forms.Form):
    searchStr = forms.CharField(max_length=100)

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('title', 'image', 'category', 'price', 'brand', 'productcode', 'rewardpoint', 'availability',
				'description')