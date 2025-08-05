from django.db import models

class Servicos_adicionais(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.valor