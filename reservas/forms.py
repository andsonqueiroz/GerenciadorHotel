from django import forms
from reservas.models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['hospede', 'quarto', 'dtEntrada', 'dtSaida', 'quantPessoas']
        widgets = {
            'hospede': forms.Select(attrs={'class': 'form-control'}),
            'quarto': forms.Select(attrs={'class': 'form-control'}),
            'dtEntrada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dtSaida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantPessoas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
