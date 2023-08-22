from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('criar_lista/', views.criar_lista, name='criar_lista'),
]
