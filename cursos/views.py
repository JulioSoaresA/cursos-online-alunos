from django.shortcuts import render, get_object_or_404, redirect
from cursos.models import Cursos
from usuarios.models import Usuarios


def curso(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    curso_a_exibir = {
        'curso': curso
    }
    return render(request, 'cursos/curso.html', curso_a_exibir)


def matricula(request, curso_id):
    if request.user.is_authenticated:
        curso = get_object_or_404(Cursos, pk=curso_id)
    pass