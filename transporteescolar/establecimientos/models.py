from django.db import models


class Establecimiento(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    comuna = models.ForeignKey('Comuna', on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return self.nombre
