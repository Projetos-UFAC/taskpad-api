from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# usando o modulo Auth do django 

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # checando caso nome seja repetido
        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')
        
        # criando usuario do database
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado')
    
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # autenticando
        user = authenticate(username = username, password = senha)

        if user:
            login(request, user) # logando no sistema

            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')