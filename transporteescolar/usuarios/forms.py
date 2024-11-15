from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(
        label='Apellidos', max_length=30, required=False)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    phone = forms.CharField(label='Teléfono', max_length=15, required=False)
    is_staff = forms.BooleanField(label='Es Staff', required=False)
    is_superuser = forms.BooleanField(label='Es Superadmin', required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'phone', 'is_staff', 'is_superuser')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
        }
