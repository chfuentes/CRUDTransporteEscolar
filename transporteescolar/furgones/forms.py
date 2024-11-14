from django import forms
from .models import Furgon


class FurgonForm(forms.ModelForm):
    class Meta:
        model = Furgon
        fields = ['patente', 'marca', 'modelo', 'año',
                  'chofer_asignado', 'establecimientos']
        widgets = {
            'establecimientos': forms.CheckboxSelectMultiple(),
        }
