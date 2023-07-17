from django.db import models


class Relatorio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.nome
   
