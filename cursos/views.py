from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from cursos.models import Cursos, Componente, Matriculado, Atividades
from usuarios.models import Usuarios
from datetime import datetime


def curso(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    matriculas = Matriculado.objects.all().filter(cpf=request.user.cpf, curso_id=curso_id).exists()
    usuarios = Usuarios.objects.all()

    curso_a_exibir = {
        'curso': curso,
        'matriculas': matriculas
    }
    return render(request, 'cursos/curso.html', curso_a_exibir)


def matricula(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    id_usuario = request.user.pk
    usuarios = Usuarios.objects.all()

    if request.user.is_authenticated and not Matriculado.objects.filter(cpf=request.user.cpf,
                                                                        curso_id=curso_id).exists():
        componentes = curso.componentes.all().order_by('ordem')
        matriculas = Matriculado.objects.all().filter(curso_id=curso_id).order_by('nome_completo')
        atividades = Atividades.objects.filter(nome_usuario=request.user)
        porcentagem_curso = 0
        atividades2 = []

        for atividade in atividades:
            atividades2.append(atividade.nome_componente)

        context = {
            'curso': curso,
            'componentes': componentes,
            'matriculas': matriculas,
            'atividades': atividades,
            'comparador_atividade': atividades2,
            'porcentagem': porcentagem_curso,
            'usuarios': usuarios,
        }
        usuario = request.user.nome_completo
        cpf = request.user.cpf
        novo_matriculado = Matriculado(id_usuario=id_usuario, nome_completo=usuario, cpf=cpf, curso_id=curso_id, porcentagem=0)
        novo_matriculado.save()
        return render(request, 'cursos/matricula.html', context)

    else:
        pk_usuario = get_object_or_404(Matriculado, cpf=request.user.cpf, curso_id=curso_id).pk
        if request.user.is_authenticated:
            componentes = curso.componentes.all().order_by('ordem').filter(curso=curso_id)
            matriculas = Matriculado.objects.all().filter(curso_id=curso_id).order_by('nome_completo')
            matricula_autenticada = get_object_or_404(Matriculado, cpf=request.user.cpf, curso_id=curso_id)
            atividades = Atividades.objects.filter(id_usuario=pk_usuario)
            atividades2 = []
            componentes_aprovados = []
            quantidade_componentes = Componente.objects.prefetch_related('curso').filter(curso=curso_id).count()

            counter = 0
            for componente in componentes:
                for atividade in atividades:
                    if componente.nome_componente == atividade.nome_componente:
                        if atividade.status == 'APROVADO':
                            componentes_aprovados.append(componente.ordem)
                            counter += 1

            porcentagem_curso = int(counter / quantidade_componentes * 100)
            if porcentagem_curso > matricula_autenticada.porcentagem:
                Matriculado.objects.filter(pk=pk_usuario).update(porcentagem=porcentagem_curso)
            porcentagem_curso = matricula_autenticada.porcentagem

            for atividade in atividades:
                atividades2.append(atividade.nome_componente)

            ultimo_componente_aprovado = -1
            if len(componentes_aprovados) > 0:
                ultimo_componente_aprovado = componentes_aprovados[-1]

            context = {
                'curso': curso,
                'componentes': componentes,
                'matriculas': matriculas,
                'matricula_autenticada': matricula_autenticada,
                'atividades': atividades,
                'comparador_atividade': atividades2,
                'porcentagem': porcentagem_curso,
                'usuarios': usuarios,
                'ultimo_componente_aprovado': ultimo_componente_aprovado,

            }
            return render(request, 'cursos/matricula.html', context)
        else:
            return render(request, 'alunos/index.html')


def envia_atividade(request, componente_id):
    componente = get_object_or_404(Componente, pk=componente_id)
    curso = componente.curso.all().first()
    if request.method == 'POST':
        if Atividades.objects.filter(nome_componente=componente, id_usuario=request.user.pk).exists():
            atividade = Atividades.objects.get(nome_componente=componente)
            atividade.delete()
            arquivo = request.FILES['envia_atividade']
            usuario = Matriculado.objects.get(cpf=request.user.cpf, curso_id=curso.id).id
            nova_avitidade = Atividades(arquivo=arquivo, id_usuario=usuario, nome_componente=componente, nome_usuario=request.user, status='AGUARDANDO_AVALIACAO')
            nova_avitidade.save()
            componente.arquivo.add(nova_avitidade)
            return redirect('dashboard')
        else:
            arquivo = request.FILES['envia_atividade']
            usuario = Matriculado.objects.get(cpf=request.user.cpf, curso_id=curso.id).id
            nova_avitidade = Atividades(arquivo=arquivo, id_usuario=usuario, nome_componente=componente, nome_usuario=request.user, status='AGUARDANDO_AVALIACAO')
            nova_avitidade.save()
            componente.arquivo.add(nova_avitidade)
            return redirect('dashboard')
    else:
        atividade = Atividades.objects.get(nome_componente=componente)
        atividade.delete()
        arquivo = request.FILES['envia_atividade']
        usuario = Matriculado.objects.get(cpf=request.user.cpf, curso_id=curso.id).id
        nova_avitidade = Atividades(arquivo=arquivo, id_usuario=usuario, nome_componente=componente, nome_usuario=request.user, status='AGUARDANDO_AVALIACAO')
        nova_avitidade.save()
        componente.arquivo.add(nova_avitidade)
        return redirect('dashboard')


def gera_certificado(request, curso_id):
    data_conclusao = datetime.now()
    curso = get_object_or_404(Cursos, pk=curso_id)
    curso_a_exibir = {
        'curso': curso,
        'conclusao': data_conclusao
    }
    return render(request, 'cursos/certificado.html', curso_a_exibir)
