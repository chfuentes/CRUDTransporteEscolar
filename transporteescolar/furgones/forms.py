from django import forms
from .models import Furgon
from django.core.exceptions import ValidationError


class FurgonForm(forms.ModelForm):
    class Meta:
        model = Furgon
        fields = ['patente', 'marca', 'modelo', 'año',
                  'chofer_asignado', 'establecimientos']
        widgets = {
            'establecimientos': forms.CheckboxSelectMultiple(),
        }

    def clean_establecimientos(self):
        establecimientos = self.cleaned_data.get('establecimientos')
        if establecimientos and establecimientos.count() > 2:
            raise ValidationError(
                "Un furgón no puede estar asociado a más de dos establecimientos.")
        return establecimientos
