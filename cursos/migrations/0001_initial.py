# Generated by Django 4.0.5 on 2023-04-04 20:39

import cursos.validation
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField(null=True, verbose_name='Id do usuário')),
                ('nome_usuario', models.CharField(max_length=150, null=True, verbose_name='Nome do aluno')),
                ('nome_componente', models.CharField(max_length=150, null=True, verbose_name='Nome do componente')),
                ('arquivo', models.FileField(upload_to='uploads/', validators=[cursos.validation.file_size], verbose_name='Atividade')),
                ('status', models.TextField(choices=[('AGUARDANDO_AVALIACAO', 'Aguardando avaliação'), ('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado')], default=0, null=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do componente')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horária')),
                ('ordem', models.IntegerField()),
                ('arquivo', models.ManyToManyField(related_name='matriculados', to='cursos.atividades', verbose_name='Atividades')),
            ],
            options={
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do curso')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('objetivo', models.TextField(verbose_name='Objetivo')),
                ('idade_minima', models.IntegerField(verbose_name='Idade mínima')),
                ('componentes', models.ManyToManyField(related_name='curso', to='cursos.componente', verbose_name='Componentes')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='TokenValidacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(max_length=32, verbose_name='Token')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField(null=True, verbose_name='Id do usuário')),
                ('nome_completo', models.CharField(max_length=150, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('porcentagem', models.IntegerField(null=True, verbose_name='Porcentagem do curso')),
                ('data_inscricao', models.DateTimeField(null=True, verbose_name='Data de inscrição')),
                ('data_conclusao', models.DateTimeField(null=True, verbose_name='Data de conclusão')),
                ('token_validacao', models.TextField(max_length=32, null=True, verbose_name='Token de validação')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cursos.cursos')),
            ],
        ),
    ]
