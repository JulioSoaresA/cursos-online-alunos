from django.shortcuts import render, redirect
from cursos.models import Cursos
from usuarios.models import Usuarios


def index(request):
    if request.user.is_authenticated:
        idade_usuario = request.user.get_idade()
        cursos = Cursos.objects.filter(idade_minima__lte=idade_usuario)
        context = {
            'cursos': cursos
        }
        return render(request, 'alunos/index.html', context)
    else:
        return render(request, 'alunos/index.html')
