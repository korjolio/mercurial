# Generated by Django 4.0.1 on 2022-01-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ape_mat',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='ape_pat',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='razon_social',
        ),
    ]
