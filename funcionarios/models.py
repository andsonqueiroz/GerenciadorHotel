from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    cargo = models.CharField(max_length=100)
    salario = models.IntegerField()

    def __str__(self):
        return self.nome