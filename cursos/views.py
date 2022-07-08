from django.shortcuts import render, get_object_or_404, redirect
from cursos.models import Cursos, Componente, Matriculado
from usuarios.models import Usuarios


def curso(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    matriculas = curso.matriculados.filter(cpf=request.user.cpf).exists()
    curso_a_exibir = {
        'curso': curso,
        'matriculas': matriculas
    }
    return render(request, 'cursos/curso.html', curso_a_exibir)


def matricula(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    if request.user.is_authenticated and not curso.matriculados.filter(cpf=request.user.cpf).exists():
        componentes = curso.componentes.all().order_by('ordem')
        matriculas = curso.matriculados.all().order_by('nome_completo')
        context = {
            'curso': curso,
            'componentes': componentes,
            'matriculas': matriculas
        }
        usuario = request.user.nome_completo
        cpf = request.user.cpf
        if not Matriculado.objects.filter(cpf=cpf).exists():
            novo_matriculado = Matriculado(nome_completo=usuario, cpf=cpf)
            novo_matriculado.save()
            curso.matriculados.add(novo_matriculado)
            print('Adicionado no banco com sucesso')
            return render(request, 'cursos/matricula.html', context)
        curso.matriculados.add(Matriculado.objects.get(cpf=request.user.cpf))
        return render(request, 'cursos/matricula.html', context)

    else:
        if request.user.is_authenticated:
            componentes = curso.componentes.all().order_by('ordem')
            matriculas = curso.matriculados.all().order_by('nome_completo')
            context = {
                'curso': curso,
                'componentes': componentes,
                'matriculas': matriculas
            }
            return render(request, 'cursos/matricula.html', context)
        else:
            return render(request, 'alunos/index.html')
