# Generated by Django 4.0.1 on 2022-01-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0002_remove_cliente_ape_mat_remove_cliente_ape_pat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_pers',
            field=models.IntegerField(choices=[(1, 'Persona Natural'), (2, 'Empresa')], default=''),
        ),
    ]
