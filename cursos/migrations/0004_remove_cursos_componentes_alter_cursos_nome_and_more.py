# Generated by Django 4.0.5 on 2022-07-07 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_cursos_componentes_alter_cursos_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='componentes',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nome',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_componente', models.CharField(max_length=150)),
                ('carga_horaria', models.IntegerField()),
                ('ordem', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos')),
            ],
        ),
    ]