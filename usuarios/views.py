from django.shortcuts import render, redirect
from usuarios.forms import Autocadastro


def autocadastro(request):
    """Cadastra uma nova pessoa no sistema"""

    if request.method == 'GET':
        form = Autocadastro()
        contexto = {'form': form}
        return render(request, 'usuarios/autocadastro.html', contexto)
    else:
        form = Autocadastro(request.POST)
        if form.is_valid():
            print(form.data['nome_completo'])
            form = Autocadastro()
            contexto = {'form': form}
            return render(request, 'usuarios/dashboard.html', contexto)
        else:
            print('Form inválido')
            contexto = {'form': form}
            return render(request, 'usuarios/autocadastro.html', contexto)


def login(request):
    """Realiza o login de uma pessoa no sistema"""

    return render(request, 'usuarios/login.html')


def dashboard(request):
    """Renderiza o deshboard do usuário"""
    if request.method == 'POST':
        form = Autocadastro(request.POST)
        contexto = {'form': form}
        return render(request, 'usuarios/dashboard.html', contexto)


def logout(request):
    """Desconecta uma pessoa do sistema"""
    return None