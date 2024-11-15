from django import forms
from .models import Furgon
from django.core.exceptions import ValidationError
import datetime


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

    def clean_año(self):
        año = self.cleaned_data.get('año')
        hoy = datetime.date.today()
        año_tope = hoy.year + 1
        if año > año_tope:
            raise ValidationError(
                f"El año no puede ser superior al {año_tope} .")
        return año
