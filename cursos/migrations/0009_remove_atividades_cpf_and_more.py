# Generated by Django 4.0.5 on 2022-07-09 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_atividades_remove_componente_arquivo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividades',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='nome_completo',
        ),
    ]