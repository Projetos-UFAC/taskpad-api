from django.shortcuts import render
from atividade.models import Atividade 

def pagina_inicial(request):
    atividades = Atividade.objects.all()  # Buscar todas as atividades
    return render(request, 'core/pagina_inicial.html', {'atividades': atividades})
