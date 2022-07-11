# Generated by Django 4.0.5 on 2022-07-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0013_rename_usuario_atividades_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividades',
            name='status',
            field=models.TextField(choices=[('AGUARDANDO_AVALIACAO', 'Aguardando avaliação'), ('APROVADO', 'Provado'), ('REPROVADO', 'Reprovado')], default=0, null=True, verbose_name='Status'),
        ),
    ]
