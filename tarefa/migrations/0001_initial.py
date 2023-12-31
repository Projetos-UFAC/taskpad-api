# Generated by Django 4.2.2 on 2023-08-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividadePrincipal', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('status', models.BooleanField()),
                ('prioridade', models.IntegerField(choices=[(1, 'Baixa'), (2, 'Média'), (3, 'Alta')])),
            ],
        ),
    ]
