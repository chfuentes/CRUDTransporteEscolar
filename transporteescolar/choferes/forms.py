from django import forms
from .models import Chofer
from django.core.exceptions import ValidationError
import re


class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['rut', 'dv', 'nombres', 'apellido_paterno', 'apellido_materno',
                  'fecha_nacimiento', 'direccion', 'comuna', 'telefono', 'email']
        # widgets = {
        #     'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        # }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'id': 'id_fecha_nacimiento', 'class': 'd-none'}),

        }
    rut = forms.CharField(
        max_length=8
    )
    telefono = forms.CharField(
        max_length=9,
        help_text="Ingrese 9 dígitos"
    )

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\d{9}$', telefono):
            raise ValidationError(
                "El número de teléfono debe tener 9 dígitos.")
        return telefono
