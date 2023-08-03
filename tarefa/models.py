from django.db import models

class Tarefa(models.Model):
    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    atividadePrincipal = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    status = models.BooleanField()
    prioridade = models.IntegerField(choices=CHOICES) 

    def __str__(self):
        return self.nome