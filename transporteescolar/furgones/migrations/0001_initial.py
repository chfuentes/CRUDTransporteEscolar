# Generated by Django 5.1.3 on 2024-11-14 19:57

import django.core.validators
import django.db.models.deletion
import furgones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choferes', '0002_chofer_email_chofer_telefono_alter_chofer_rut'),
        ('establecimientos', '0002_add_comunas_linares'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furgon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=6, unique=True, validators=[furgones.models.Furgon.validate_patente])),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2010), django.core.validators.MaxValueValidator(2050)])),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('chofer_asignado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='choferes.chofer')),
                ('establecimientos', models.ManyToManyField(blank=True, to='establecimientos.establecimiento')),
            ],
        ),
    ]
