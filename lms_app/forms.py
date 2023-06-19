from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }





class BookForm (forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'title',
            'athour',
            'photo_book',
            'photo_athour',
            'pages_book',
            'starus',
            'price',
            'rental_price_inday',
            'rebtal_time',
            'total_rental',
            'category',
            ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'athour':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_athour':forms.FileInput(attrs={'class':'form-control'}),
            'pages_book':forms.NumberInput(attrs={'class':'form-control'}),
            'starus':forms.Select(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'rental_price_inday':forms.NumberInput(attrs={'class':'form-control',"id":"ri"}),
            'rebtal_time':forms.NumberInput(attrs={'class':'form-control',"id":"rt"}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control',"id":"tr"}),
            'category':forms.Select(attrs={'class':'form-control'}),
            }



