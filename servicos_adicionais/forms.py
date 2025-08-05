from django.forms import ModelForm
from .models import Servicos_adicionais
from django import forms
from django.db import models

class ServicosForm(forms.ModelForm):
    class Meta:
        model = Servicos_adicionais
        fields = ['tipo', 'valor', 'descricao']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o tipo, ex: lavanderia, café, etc...'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o valor'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Descreva o funcionamento do serviço'}),    
        }

class EditServicosForm(forms.ModelForm):
    class Meta:
        model = Servicos_adicionais
        fields = ['tipo', 'valor', 'descricao']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o tipo, ex: lavanderia, café, etc...'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o valor'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Descreva o funcionamento do serviço'}),    
        }
                