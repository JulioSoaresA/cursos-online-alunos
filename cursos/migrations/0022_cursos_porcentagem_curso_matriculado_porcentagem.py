# Generated by Django 4.0.5 on 2022-07-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0021_alter_atividades_arquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='porcentagem_curso',
            field=models.ManyToManyField(related_name='porcentagem_curso', to='cursos.matriculado'),
        ),
        migrations.AddField(
            model_name='matriculado',
            name='porcentagem',
            field=models.IntegerField(null=True, verbose_name='Porcentagem do curso'),
        ),
    ]
