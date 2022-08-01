from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import auth, messages
from .models import Usuarios
from usuarios.forms import Autocadastro
from cursos.models import Matriculado


def autocadastro(request):
    """Cadastra uma nova pessoa no sistema"""

    if request.method == 'GET':
        form = Autocadastro()
        contexto = {'form': form}
        return render(request, 'usuarios/autocadastro.html', contexto)
    else:
        form = Autocadastro(request.POST)
        if form.is_valid():
            form = Autocadastro()
            contexto = {'form': form}
            nome_completo = request.POST['nome_completo']
            cpf = request.POST['cpf']
            data_nascimento = request.POST['data_nascimento']
            privacidade = request.POST['indica_privacidade']
            senha = request.POST['password']
            user = Usuarios.objects.create_user(cpf=cpf, nome_completo=nome_completo, data_nascimento=data_nascimento, indica_privacidade=privacidade, password=senha)
            user.save()
            messages.success(request, 'Cadastrado realizado com sucesso')
            return render(request, 'usuarios/autocadastro.html', contexto)
        else:
            print('Form inválido')
            contexto = {'form': form}
            return render(request, 'usuarios/autocadastro.html', contexto)


def login(request):
    """Realiza o login de uma pessoa no sistema"""
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['password']
        if cpf == "" or senha == "":
            messages.error(request, 'Os campos CPF e Senha não podem ficar em branco.')
            return redirect('login')
        if Usuarios.objects.filter(cpf=cpf).exists():
            user = auth.authenticate(request, cpf=cpf, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'CPF ou senha incorreto.')
                return redirect('login')
        else:
            messages.error(request, 'CPF ou senha incorreto.')
            return redirect('login')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    """Renderiza o deshboard do usuário"""
    matriculado = Matriculado.objects.all().filter(id_usuario=request.user.pk).exists()
    if request.user.is_authenticated and matriculado:
        cursos_usuario = get_list_or_404(Matriculado.objects.all().filter(cpf=request.user.cpf).order_by('curso_id'))
        context = {
            'cursos_usuario': cursos_usuario
        }

        return render(request, 'usuarios/dashboard.html', context)
    else:

        return redirect('index')


def logout(request):
    """Desconecta uma pessoa do sistema"""
    auth.logout(request)
    return redirect('index')
