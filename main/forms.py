<<<<<<< HEAD
from django import forms

class UserForm(forms.Form):
    searchStr = forms.CharField(max_length=100)
=======
from django import forms

from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)
>>>>>>> 35b5e9da8da2ec4683feb7298cb2ae155664f37c
