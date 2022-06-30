from django.shortcuts import render
from usuarios.forms import Autocadastro


def autocadastro(request):
    """Cadastra uma nova pessoa no sistema"""
    form = Autocadastro()
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