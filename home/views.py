from django.shortcuts import render
from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

@login_required(login_url="/auth/login/")
def pagina_inicial(request):
    if request.user.is_authenticated:
        listas = Lista.objects.all()
        atividades = Atividade.objects.all()
        tarefas = Tarefa.objects.all()
        
        return render(request, 'pagina_inicial.html', {'listas': listas, 'atividades': atividades, 'tarefas': tarefas})
    else:
        return HttpResponse('Voce precisa estar logado')