from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Usuario o contraseña inválida.")

        # Custom validation for email format
        email = cleaned_data.get('username')
        print("email: ", email)
        if email is not None:
            if '@' not in email:
                raise ValidationError("El correo no contiene '@'")
            print(email)
            _, domain = email.split('@')
            # Add more email format validation if needed
            if '.' not in domain:
                raise ValidationError("El correo no presenta dominio")
        
            _, com= domain.split('.')
        return cleaned_data





