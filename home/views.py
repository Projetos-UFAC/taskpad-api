from django.shortcuts import render, redirect
from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.utils.dateparse import parse_date

@login_required(login_url="/auth/login/")
def pagina_inicial(request):
    if request.user.is_authenticated:
        listas = Lista.objects.filter(user=request.user) # pegando apenas do usuario logado
        atividades = Atividade.objects.filter(user=request.user)
        tarefas = Tarefa.objects.filter(user=request.user)
        
        return render(request, 'pagina_inicial.html', {'listas': listas, 'atividades': atividades, 'tarefas': tarefas})
    else:
        return HttpResponse('Voce precisa estar logado')
    
# pop up p criar lista
def criar_lista(request):
    if request.method == "POST":
        nome_lista = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        dataInicio = request.POST.get('dataInicio')
        dataFim = request.POST.get('dataFim')
        prioridade = request.POST.get('prioridade')
        status = request.POST.get('status')
        
        # Converte status em um valor booleano
        status = True if status == 'on' else False
        
        user = request.user

        # Convertendo as datas para o formato YYYY-MM-DD ou deixando-as como None se estiverem em branco
        # caso o user queira deixar sem
        if dataInicio:
            dataInicio = parse_date(dataInicio)
        else:
            dataInicio = None
        
        if dataFim:
            dataFim = parse_date(dataFim)
        else:
            dataFim = None

        nova_lista = Lista(
            user=user,
            nome=nome_lista,
            descricao=descricao,
            dataInicio=dataInicio,
            dataFim=dataFim,
            prioridade=prioridade,
            status=status
        )
        nova_lista.save()

        return redirect('pagina_inicial')  # Redirecionar de volta à página inicial

    return render(request, 'criar_lista.html')  # Caso GET, renderizar o formulário



def criar_atividade(request):
    if request.method == "POST":
        user = request.user
        lista_id = request.POST.get('lista_id')  # Passe o ID da lista através do formulário
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        dataInicio = request.POST.get('dataInicio')
        dataFim = request.POST.get('dataFim')
        status = False  # Defina um valor padrão para o status
        prioridade = request.POST.get('prioridade')

        nova_atividade = Atividade(
            user=user,
            lista_id=lista_id,
            nome=nome,
            descricao=descricao,
            dataInicio=dataInicio,
            dataFim=dataFim,
            status=status,
            prioridade=prioridade
        )
        nova_atividade.save()

        return redirect('pagina_inicial')  # Redirecionar para a página inicial após a criação da atividade

    return render(request, 'criar_atividade.html')  # Caso GET, renderizar o formulário