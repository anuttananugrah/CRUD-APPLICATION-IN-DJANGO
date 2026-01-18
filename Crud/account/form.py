from django import forms
from account.models import ProductModel

class ProductsModelForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields=("__all__")
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter Product Title','class':'form-control'}),
            'description':forms.TextInput(attrs={'placeholder':'Enter Product Description','class':'form-control '}),
            'price':forms.TextInput(attrs={'placeholder':'Enter Price','class':'form-control '}),
            'category':forms.Select(attrs={'class':'form-control ', 'style':'background-color: rgba(255,255,255,0.5)'})
        }