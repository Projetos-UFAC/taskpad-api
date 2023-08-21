from django.db import models

# Agora Lista, Atividade e Tarefa tem comportamentos quase iguais pois os mesmos podem ser editados como arquivos de texto
class Lista(models.Model):
    CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    status = models.BooleanField()
    prioridade = models.IntegerField(choices=CHOICES) 
    texto = models.TextField(default=' ')
    
    def __str__(self):
        return self.nome
   
