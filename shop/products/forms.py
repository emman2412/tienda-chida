from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'trademark', 'price', 'category', 'description', 'image', 'stock',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del producto'}),
            'trademark': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio del producto'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Imagen del producto'}),
            'stock': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Unidades en existencia'}),
        }