from django import forms
from products import models

class NewProductForm(forms.ModelForm):
    class Meta():
        model = models.Product
        fields = '__all__'