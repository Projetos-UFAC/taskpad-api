from django.db import models
from lista.models import Lista

class Atividade(models.Model):

    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, default=1)  # Chave estrangeira para Lista
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    status = models.BooleanField()
    prioridade = models.IntegerField(choices=CHOICES) #Aqui é IntegerField
    texto = models.TextField(default=' ') #Pelo jeito o django precisa de um valor padrão aq

    def __str__(self):
        return self.nome
