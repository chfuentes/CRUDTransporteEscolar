# Generated by Django 5.1.3 on 2024-11-14 15:18

from django.db import migrations


def add_comunas_linares(apps, schema_editor):
    Comuna = apps.get_model('establecimientos', 'Comuna')
    comunas = [
        "Linares",
        "San Javier",
        "Villa Alegre",
        "Yerbas Buenas",
        "Colbún",
        "Longaví",
        "Parral",
        "Retiro"
    ]
    for nombre in comunas:
        Comuna.objects.create(nombre=nombre, estado='A')


class Migration(migrations.Migration):

    dependencies = [
        ('establecimientos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_comunas_linares),

    ]
