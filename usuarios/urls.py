from django.urls import path
from . import views

urlpatterns = [
    path('', views.aplicacao, name ='aplicacao'), # definindo a pagina principal de login
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('login/', views.login, name='login'),
    path('aplicacao/', views.aplicacao, name='aplicacao' )
    ]