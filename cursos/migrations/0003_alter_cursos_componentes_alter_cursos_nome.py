# Generated by Django 4.0.5 on 2022-07-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_cursos_componentes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='componentes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nome',
            field=models.TextField(),
        ),
    ]