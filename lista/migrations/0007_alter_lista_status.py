# Generated by Django 4.2.3 on 2023-09-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lista", "0006_alter_lista_texto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lista",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
