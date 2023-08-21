from django.db import models
from atividade.models import Atividade

class Tarefa(models.Model):
    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, default=1)  # Chave estrangeira para Atividade
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    status = models.BooleanField()
    prioridade = models.IntegerField(choices=CHOICES) 
    texto = models.TextField(default=' ')

    def __str__(self):
        return self.nome