from django.http import HttpResponse
from django.shortcuts import redirect, render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from django.http import HttpResponse

from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
@extend_schema(
    description="Página inicial que mostra listas, atividades e tarefas do usuário logado.",
    responses={200: "Lista de objetos JSON contendo informações das listas, atividades e tarefas."}
)
@login_required(login_url="/auth/login/")
def pagina_inicial(request):
    if request.user.is_authenticated:
        listas = Lista.objects.filter(user=request.user)
        atividades = Atividade.objects.filter(user=request.user)
        tarefas = Tarefa.objects.filter(user=request.user)
        
        return render(request, 'pagina_inicial.html', {'listas': listas, 'atividades': atividades, 'tarefas': tarefas})
    else:
        return HttpResponse('Você precisa estar logado')

class CriarListaView(APIView):
    @extend_schema(
        description="Cria uma nova lista.",
        request="Objeto JSON contendo informações da nova lista.",
        responses={201: "Objeto JSON contendo informações da nova lista criada."}
    )
    def post(self, request):
        """
        Cria uma nova lista.
        """
        if request.method == "POST":
            nome_lista = request.data.get('nome')
            descricao = request.data.get('descricao')
            dataInicio = request.data.get('dataInicio')
            dataFim = request.data.get('dataFim')
            prioridade = request.data.get('prioridade')
            status = request.data.get('status')
            
            status = True if status == 'on' else False
            
            user = request.user

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

            return redirect('pagina_inicial')

class CriarAtividadeView(APIView):
    @extend_schema(
        description="Cria uma nova atividade.",
        request="Objeto JSON contendo informações da nova atividade.",
        responses={201: "Objeto JSON contendo informações da nova atividade criada."}
    )
    def post(self, request):
        """
        Cria uma nova atividade.
        """
        if request.method == "POST":
            user = request.user
            lista_id = request.data.get('lista_id')
            nome_atividade = request.data.get('nome_atividade')
            descricao = request.data.get('descricao')
            dataInicio = request.data.get('dataInicio')
            dataFim = request.data.get('dataFim')
            status = request.data.get('status')
            prioridade = request.data.get('prioridade')

            status = True if status == 'on' else False
            
            if dataInicio:
                dataInicio = parse_date(dataInicio)
            else:
                dataInicio = None
            
            if dataFim:
                dataFim = parse_date(dataFim)
            else:
                dataFim = None

            nova_atividade = Atividade(
                user=user,
                lista_id=lista_id,
                nome=nome_atividade,
                descricao=descricao,
                dataInicio=dataInicio,
                dataFim=dataFim,
                status=status,
                prioridade=prioridade
            )
            nova_atividade.save()

            return redirect('pagina_inicial')
        
class CriarTarefaView(APIView):
    @extend_schema(
        description="Cria uma nova tarefa.",
        request="Objeto JSON contendo informações da nova tarefa.",
        responses={201: "Objeto JSON contendo informações da nova tarefa criada."}
    )
    def post(self, request):
        """
        Cria uma nova tarefa.
        """
        if request.method == "POST":
            user = request.user
            atividade_id = request.data.get('atividade_id')
            nome_tarefa = request.data.get('nome_tarefa')
            descricao = request.data.get('descricao')
            dataInicio = request.data.get('dataInicio')
            dataFim = request.data.get('dataFim')
            status = request.data.get('status')
            prioridade = request.data.get('prioridade')

            status = True if status == 'on' else False
            
            if dataInicio:
                dataInicio = parse_date(dataInicio)
            else:
                dataInicio = None
            
            if dataFim:
                dataFim = parse_date(dataFim)
            else:
                dataFim = None

            nova_tarefa = Tarefa(
                user=user,
                atividade_id=atividade_id,
                nome=nome_tarefa,
                descricao=descricao,
                dataInicio=dataInicio,
                dataFim=dataFim,
                status=status,
                prioridade=prioridade
            )
            nova_tarefa.save()

            return redirect('pagina_inicial')
