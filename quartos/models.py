from django.db import models

class Quarto(models.Model):
    numero = models.IntegerField(unique=True, primary_key=True)
    tipo = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    disponibilidade = models.BooleanField(default=True)
    preco_diaria = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Quarto nº {self.numero} - {self.tipo}"