# Generated by Django 4.2.3 on 2023-08-24 02:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0005_alter_lista_datafim_alter_lista_datainicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
