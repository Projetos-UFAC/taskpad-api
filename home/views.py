from django.shortcuts import render, redirect
from lista.models import Lista
from atividade.models import Atividade
from tarefa.models import Tarefa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.utils.dateparse import parse_date
from .forms import ListaForm, AtividadeForm, TarefaForm
from ckeditor.fields import RichTextFormField
from django.shortcuts import get_object_or_404


@login_required(login_url="/auth/login/")
def pagina_inicial(request):


    if request.user.is_authenticated:
        listas = Lista.objects.filter(user=request.user)
        atividades = Atividade.objects.filter(user=request.user)
        tarefas = Tarefa.objects.filter(user=request.user)
        texto_form = RichTextFormField()

        if request.method == "POST":
            lista_form = ListaForm(request.POST)
            atividade_form = AtividadeForm(request.POST)
            tarefa_form = TarefaForm(request.POST)
            
            object_type = request.POST.get('object_type')
            item_id = request.POST.get('object_id')

            # programando puto essa função aqui, mermão... não altere nada se n tiver certeza de que irá funcionar!
            
            if object_type and item_id:  # Verifique se há um tipo de objeto e um ID válido
                if object_type == 'lista':
                    obj = get_object_or_404(Lista, id=item_id)
                    obj.texto = request.POST.get('conteudo_atividade')
                    obj.save()
                elif object_type == 'atividade':
                    obj = get_object_or_404(Atividade, id=item_id)
                    obj.texto = request.POST.get('conteudo_atividade')
                    obj.save()
                elif object_type == 'tarefa':
                    obj = get_object_or_404(Tarefa, id=item_id)
                    obj.texto = request.POST.get('conteudo_atividade')
                    obj.save()

        else:
            lista_form = ListaForm()
            atividade_form = AtividadeForm()
            tarefa_form = TarefaForm()

        return render(request, 'pagina_inicial.html', {
            'listas': listas,
            'atividades': atividades,
            'tarefas': tarefas,
            'lista_form': lista_form,
            'atividade_form': atividade_form,
            'tarefa_form': tarefa_form,
            'texto_form': texto_form, 
        })
    else:
        return HttpResponse('Você precisa estar logado')
  
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
        nome_atividade = request.POST.get('nome_atividade')
        descricao = request.POST.get('descricao')
        dataInicio = request.POST.get('dataInicio')
        dataFim = request.POST.get('dataFim')
        status = False  # Defina um valor padrão para o status
        prioridade = request.POST.get('prioridade')


        # Converte status em um valor booleano
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

        return redirect('pagina_inicial')  # Redirecionar para a página inicial após a criação da atividade

    return render(request, 'criar_atividade.html')  # Caso GET, renderizar o formulário


def criar_tarefa(request):
    if request.method == "POST":
        user = request.user
        atividade_id = request.POST.get('atividade_id')  # Passe o ID da atividade através do formulário
        nome_tarefa = request.POST.get('nome_tarefa')
        descricao = request.POST.get('descricao')
        dataInicio = request.POST.get('dataInicio')
        dataFim = request.POST.get('dataFim')
        status = False  # Defina um valor padrão para o status
        prioridade = request.POST.get('prioridade')

        # Converte status em um valor booleano
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

        return redirect('pagina_inicial')  # Redirecionar para a página inicial após a criação da tarefa

    return render(request, 'criar_tarefa.html')  # Caso GET, renderizar o formulário


from django.http import JsonResponse

def deletar_item(request):
    if request.method == 'POST':
        objectType = request.POST.get('objectType')
        itemId = request.POST.get('itemId')

        if objectType and itemId:
            if objectType == 'lista':
                    lista = get_object_or_404(Lista, id=itemId)
                    
                    # atividades e tarefas associadas à lista
                    for atividade in lista.atividade_set.all():
                        for tarefa in atividade.tarefa_set.all():
                            tarefa.delete()
                        atividade.delete()
                    
                    lista.delete()

            elif objectType == 'atividade':
                obj = get_object_or_404(Atividade, id=itemId)
                
                # Exclua as tarefas associadas à atividade
                for tarefa in obj.tarefa_set.all():
                    tarefa.delete()
                
                obj.delete()

            elif objectType == 'tarefa':
                obj = get_object_or_404(Tarefa, id=itemId)
                obj.delete()

        return redirect('pagina_inicial')  # 
        # Para depurar...
        #     return JsonResponse({'message': 'Item excluído com sucesso'})
        # else:
        #     return JsonResponse({'message': 'Dados inválidos'})
    else:
        return redirect('pagina_inicial')  # 
