from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from establecimientos.models import Establecimiento
from django.core.exceptions import ValidationError
from choferes.models import Chofer
import re


class Furgon(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    def validate_patente(value):
        if not re.match(r'^[BCDFGHJKLMNPQRSTVWXYZ]{4}\d{2}$', value):
            raise ValidationError(
                '%(value)s no es un formato de patente válido. Debe ser 4 letras (sin vocales) seguidas de 2 números.',
                params={'value': value},
            )

    def validate_establecimientos(value):
        if value.count() > 3:
            raise ValidationError(
                'Un furgón no puede estar asociado a más de 3 establecimientos.')

    patente = models.CharField(
        max_length=6, unique=True, validators=[validate_patente])
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(2050)])
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='A')
    chofer_asignado = models.ForeignKey(
        Chofer, on_delete=models.SET_NULL, null=True, blank=True)
    establecimientos = models.ManyToManyField(
        Establecimiento, blank=True)

    def clean(self):
        super().clean()
        if self.establecimientos.count() > 3:
            raise ValidationError(
                'Un furgón no puede estar asociado a más de 3 establecimientos.')

    def __str__(self):
        return self.patente
