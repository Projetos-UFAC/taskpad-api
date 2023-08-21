from django.shortcuts import render
from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa

def pagina_inicial(request):
    listas = Lista.objects.all()
    atividades = Atividade.objects.all()
    tarefas = Tarefa.objects.all()
    
    return render(request, 'pagina_inicial.html', {'listas': listas, 'atividades': atividades, 'tarefas': tarefas})
