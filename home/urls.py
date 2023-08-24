from django.urls import path
from .views import pagina_inicial, CriarListaView, CriarAtividadeView, CriarTarefaView


urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('criar_lista/', CriarListaView.as_view(), name='criar_lista'),
    path('criar_atividade/', CriarAtividadeView.as_view(), name='criar_atividade'),
    path('criar_tarefa/', CriarTarefaView.as_view(), name='criar_tarefa'),  # Adicione esta linha
]
