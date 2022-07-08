from django.db import models


class Componente(models.Model):
    nome_componente = models.CharField(max_length=150)
    carga_horaria = models.IntegerField()
    ordem = models.IntegerField()

    def __str__(self):
        return self.nome_componente


class Cursos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    objetivo = models.TextField()
    carga_horaria_total = property(lambda self: sum(comp.carga_horaria for comp in self.componentes.all()))
    idade_minima = models.IntegerField()
    componentes = models.ManyToManyField(Componente, related_name='cursos')

    def __str__(self):
        return self.nome
