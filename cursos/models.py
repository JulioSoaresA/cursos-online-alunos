from django.db import models
from django.utils.translation import gettext_lazy as _
from cursos.validation import file_size



class StatusAtividade(models.TextChoices):
    AGUARDANDO_AVALIACAO = 'AGUARDANDO_AVALIACAO', _('Aguardando avaliação')
    APROVADO = 'APROVADO', _('Aprovado')
    REPROVADO = 'REPROVADO', _('Reprovado')


class Atividades(models.Model):
    id_usuario = models.IntegerField(verbose_name='Id do usuário', null=True)
    nome_usuario = models.CharField(verbose_name='Nome do aluno', max_length=150, null=True)
    nome_componente = models.CharField(verbose_name='Nome do componente', max_length=150, null=True)
    arquivo = models.FileField(verbose_name='Atividade', upload_to='uploads/', validators=[file_size])
    status = models.TextField(verbose_name='Status', choices=StatusAtividade.choices, default=0, null=True)

    def __str__(self):
        return self.nome_componente


class Componente(models.Model):
    nome = models.CharField(verbose_name='Nome do componente', max_length=150)
    carga_horaria = models.IntegerField(verbose_name='Carga horária')
    arquivo = models.ManyToManyField(Atividades, verbose_name='Atividades', related_name='matriculados')
    ordem = models.IntegerField()

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.nome_componente


class Cursos(models.Model):
    class Meta:
        verbose_name_plural = 'Cursos'

    nome = models.CharField(verbose_name='Nome do curso', max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    objetivo = models.TextField(verbose_name='Objetivo')
    carga_horaria_total = property(lambda self: sum(comp.carga_horaria for comp in self.componentes.all()))
    idade_minima = models.IntegerField(verbose_name='Idade mínima')
    componentes = models.ManyToManyField(Componente, verbose_name='Componentes', related_name='curso')

    def __str__(self):
        return self.nome


class Matriculado(models.Model):
    id_usuario = models.IntegerField(verbose_name='Id do usuário', null=True)
    nome_completo = models.CharField(verbose_name='Nome completo', max_length=150)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, related_name='cursos')
    porcentagem = models.IntegerField(verbose_name='Porcentagem do curso', null=True)
    data_inscricao = models.DateTimeField(verbose_name='Data de inscrição', null=True)
    data_conclusao = models.DateTimeField(verbose_name='Data de conclusão', null=True)
    token_validacao = models.TextField(verbose_name='Token de validação', max_length=32, null=True)

    def __str__(self):
        return self.nome_completo


class TokenValidacao(models.Model):
    token = models.TextField(verbose_name='Token', max_length=32)
