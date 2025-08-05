from django.db import models

class Hospede(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=False)
    cpf = models.CharField(primary_key=True, max_length=14)

    def __str__(self):
        return self.nome