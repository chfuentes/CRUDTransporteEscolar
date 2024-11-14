from django import forms
from .models import Chofer


class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['rut', 'dv', 'nombres', 'apellido_paterno', 'apellido_materno',
                  'fecha_nacimiento', 'direccion', 'comuna', 'telefono', 'email']
        widgets = {
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }
