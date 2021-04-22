# yourapp.forms.py
from django import forms

class JoinForm(forms.Form): # or forms.ModelForm
    image = forms.ImageField()
    name = forms.CharField(max_length=120)
    description=forms.CharField(widget=forms.TextInput())