from django.forms import ModelForm
from .models import Funcionario
from django import forms
from django.db import models

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'cargo', 'salario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do funcionário'}),
            'cpf': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cargo'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o salário'}),
        }

class EditFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'cargo', 'salario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do funcionário'}),
            'cpf': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cargo'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o salário'}),
        }
                