# Generated by Django 4.0.5 on 2022-07-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_componente_options_componente_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150, verbose_name='Nome compoeto')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('arquivo', models.FileField(upload_to='pdf/', verbose_name='Atividade')),
            ],
        ),
        migrations.RemoveField(
            model_name='componente',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='componente',
            name='arquivo',
            field=models.ManyToManyField(related_name='atividades', to='cursos.atividades', verbose_name='Atividades'),
        ),
    ]