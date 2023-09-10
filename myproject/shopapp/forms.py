from django import forms
from shopapp import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['name', 'desc', 'price', 'img']
    