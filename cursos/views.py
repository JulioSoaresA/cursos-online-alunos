import json
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cursos.models import Cursos, Componente, Matriculado, Atividades, TokenValidacao
from .forms import CaptchaForm
from usuarios.models import Usuarios
from datetime import datetime
import secrets


def curso(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    matriculas = Matriculado.objects.all().filter(cpf=request.user.cpf, curso_id=curso_id).exists()

    curso_a_exibir = {
        'curso': curso,
        'matriculas': matriculas
    }
    return render(request, 'cursos/curso.html', curso_a_exibir)


def matricula(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    id_usuario = request.user.pk
    usuarios = Usuarios.objects.all()

    if request.user.is_authenticated and not Matriculado.objects.filter(cpf=request.user.cpf, curso_id=curso_id).exists():
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
        novo_matriculado = Matriculado(id_usuario=id_usuario, nome_completo=usuario, cpf=cpf, curso_id=curso_id, porcentagem=0, data_inscricao=datetime.now())
        novo_matriculado.save()
        return render(request, 'cursos/matricula.html', context)

    else:
        pk_usuario = request.user.pk
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
                Matriculado.objects.filter(curso_id=curso_id, cpf=request.user.cpf).update(porcentagem=porcentagem_curso)
            porcentagem_curso = matricula_autenticada.porcentagem

            if porcentagem_curso == 100:
                token = secrets.token_hex(16)
                valida_token = TokenValidacao.objects.all().filter(token=token).exists()
                usuario = get_object_or_404(Matriculado.objects.all().filter(curso_id=curso_id, id_usuario=request.user.pk))
                if valida_token:
                    token = secrets.token_hex(16)

                if usuario.token_validacao == None:
                    novo_token = TokenValidacao(token=token)
                    novo_token.save()
                    Matriculado.objects.filter(curso_id=curso_id, cpf=request.user.cpf).update(data_conclusao=datetime.now(), token_validacao=token)

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
    print(request.Form)
    atv_enviada = request.FILES['envia_atividade']
    print(atv_enviada.size)
    if request.method == 'POST':

        arquivo = request.FILES['envia_atividade']

        if Atividades.objects.filter(nome_componente=componente, id_usuario=request.user.pk).exists():
            atividade = Atividades.objects.get(nome_componente=componente)
            atividade.delete()
            id_usuario = request.user.pk
            nova_avitidade = Atividades(arquivo=arquivo, id_usuario=id_usuario, nome_componente=componente, nome_usuario=request.user, status='AGUARDANDO_AVALIACAO')
            nova_avitidade.save()
            componente.arquivo.add(nova_avitidade)
            return redirect('dashboard')
        else:
            '''if arquivo.size > 1 * 1024 * 1024:
                messages.error(request, 'Arquivo muito grande. Tamanho máximo: 1MB')'''
            print()
            arquivo = request.FILES['envia_atividade']
            id_usuario = request.user.pk
            nova_avitidade = Atividades(arquivo=arquivo, id_usuario=id_usuario, nome_componente=componente, nome_usuario=request.user, status='AGUARDANDO_AVALIACAO')
            nova_avitidade.save()
            componente.arquivo.add(nova_avitidade)
            return redirect('dashboard')
    else:
        return redirect('dashboard')


def gera_certificado(request, curso_id):
    matricula = get_object_or_404(Matriculado.objects.all().filter(id_usuario=request.user.pk, curso_id=curso_id))
    data_inscricao = matricula.data_inscricao
    data_conclusao = matricula.data_conclusao
    token = matricula.token_validacao
    curso = get_object_or_404(Cursos, pk=curso_id)
    curso_a_exibir = {
        'curso': curso,
        'inscricao': data_inscricao,
        'conclusao': data_conclusao,
        'token': token,
    }
    return render(request, 'cursos/certificado.html', curso_a_exibir)


def valida_certificado(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        token_enviado = request.POST['token']
        captcha_token = request.POST.get("g-recaptcha-response")
        captcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        captcha_secret = '6LfHUjghAAAAALAyVR0ia2muNZ6CC5wBLD5hHJ_F'
        captcha_data = {
            'secret': captcha_secret,
            'response': captcha_token
        }
        contexto = {
            'form': form
        }
        captcha_server_responde = requests.post(url=captcha_url, data=captcha_data)
        captcha_json = json.loads(captcha_server_responde.text)
        if captcha_json['success'] == False:
            messages.error(request, 'reCAPTCHA inválido')
            return render(request, 'cursos/validar_certificado.html', contexto)
        validacao = TokenValidacao.objects.all().filter(token=token_enviado).exists()
        if validacao:
            messages.success(request, 'Certificado válido')
        else:
            messages.error(request, 'Certificado inválido')
        return render(request, 'cursos/validar_certificado.html', contexto)

    else:
        contexto = {
            'form': CaptchaForm
        }
        return render(request, 'cursos/validar_certificado.html', contexto)

