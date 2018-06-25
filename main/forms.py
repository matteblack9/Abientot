from django import forms
from .models import Cart

class UserForm(forms.Form):
    searchStr = forms.CharField(max_length=100)

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)

