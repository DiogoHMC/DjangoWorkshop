from django import forms
from django.forms import ModelForm
from .models import Produto

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'