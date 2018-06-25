from django import forms

class UserForm(forms.Form):
    searchStr = forms.CharField(max_length=100)
