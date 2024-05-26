from django import forms
from .models import User

# permite crear formularios basados en modelos de la base de datos.
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'password': 'Contraseña',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El usuario ya está registrado con este correo electrónico.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError("La contraseña debe tener al menos 4 caracteres.")
        return password