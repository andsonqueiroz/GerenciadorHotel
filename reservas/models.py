
from django.db import models
from clientes.models import Hospede
from quartos.models import Quarto
from datetime import timedelta

class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, to_field='cpf', on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    dtEntrada = models.DateField()
    dtSaida = models.DateField()
    quantPessoas = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def calcular_total(self):
        dias = (self.dtSaida - self.dtEntrada).days
        if dias < 1:
            dias = 1 
        return dias * self.quarto.preco_diaria

    def save(self, *args, **kwargs):

        self.valor_total = self.calcular_total()
        
        self.hospede.ativo = True
        self.hospede.save()

        self.quarto.disponibilidade = False
        self.quarto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Reserva de {self.hospede.nome} no quarto {self.quarto.numero}'
