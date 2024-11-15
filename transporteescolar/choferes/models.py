from django.db import models
from establecimientos.models import Comuna
from django.core.validators import RegexValidator


class Chofer(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    DV_CHOICES = [(str(i), str(i)) for i in range(10)] + [('K', 'K')]

    rut = models.PositiveIntegerField(
        unique=True,
        validators=[RegexValidator(
            regex=r'^\d{7,8}$', message='El RUT debe tener entre 7 y 8 dígitos')]
    )
    dv = models.CharField(max_length=1, choices=DV_CHOICES)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    telefono = models.CharField(
        max_length=12,
        validators=[RegexValidator(
            regex=r'^\+56\d{9}$', message='El teléfono debe tener el formato +56XXXXXXXXX')],
        default=None
    )
    email = models.EmailField(default=None)
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
