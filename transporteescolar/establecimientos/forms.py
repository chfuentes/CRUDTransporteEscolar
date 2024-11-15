from django import forms
from .models import Establecimiento
from django.core.exceptions import ValidationError
import re


class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ['nombre', 'direccion', 'telefono', 'comuna', 'email']

    telefono = forms.CharField(
        max_length=9,
        help_text="Ingrese 9 dígitos"
    )

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        # Si el teléfono contiene +56, eliminar el prefijo para mostrar solo 9 dígitos en el formulario
        # if telefono.startswith('+56'):
        #    telefono = telefono[3:]

        # Validar que el teléfono tenga exactamente 9 dígitos
        if not re.match(r'^\d{9}$', telefono):
            raise ValidationError(
                "El número de teléfono debe tener 9 dígitos.")

        # Retornar el teléfono con el prefijo +56 agregado
        return telefono
