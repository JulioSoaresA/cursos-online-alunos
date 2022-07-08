from django.db import models


class Matriculado(models.Model):
    nome_completo = models.CharField(verbose_name='Nome completo', max_length=150)
    cpf = models.CharField(verbose_name='CPF', max_length=11)

    def __str__(self):
        return self.nome_completo


class Componente(models.Model):
    nome_componente = models.CharField(verbose_name='Nome do componente', max_length=150)
    carga_horaria = models.IntegerField(verbose_name='Carga horária')
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
    componentes = models.ManyToManyField(Componente, related_name='cursos', verbose_name='Componentes')
    matriculados = models.ManyToManyField(Matriculado, related_name='matricula')

    def __str__(self):
        return self.nome
