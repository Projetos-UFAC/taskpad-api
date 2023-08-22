from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('criar_lista/', views.criar_lista, name='criar_lista'),
    path('criar_atividade/', views.criar_atividade, name='criar_atividade'),  # Adicione esta linha
]