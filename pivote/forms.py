from django import forms
from .models import User, Pregunta, Test
from django.contrib.auth import authenticate
from django.forms import inlineformset_factory

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Nombre',
            'email': 'Correo',
            'password': 'Contraseña',
        }

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if User.objects.filter(name=name).exists():
            raise forms.ValidationError("Un usuario ya está registrado con este nombre.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un usuario ya está registrado con este correo electrónico.")
        return email

    def clean_password(self):
        minuscula = False
        mayuscula = False
        numero = False
        password = self.cleaned_data.get('password')
        name = self.cleaned_data.get('name')
        if len(password) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        for minus in password:
            if minus.islower():
                minuscula = True
        if not minuscula:
            raise forms.ValidationError("La contraseña debe tener al menos una minuscula.")
        for mayus in password:
            if mayus.isupper():
                mayuscula = True
        if not mayuscula:
            raise forms.ValidationError("La contraseña debe tener al menos una mayuscula.")
        for num in password:
            if num.isdigit():
                numero = True
        if not numero:
            raise forms.ValidationError("La contraseña debe tener al menos un numero.")
        if password.count(name):
            raise forms.ValidationError("La contraseña no debe coincidir con su nombre.")
        return password


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'titulo', 'tema'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'enunciado', 'opcionA','opcionB','opcionC','opcionD', 'correcta'
        ]
    
        widgets = {
            'enunciado': forms.TextInput(attrs={'class': 'form-control'}),
            'opcionA': forms.TextInput(attrs={'class': 'form-control'}),
            'opcionB': forms.TextInput(attrs={'class': 'form-control'}),
            'opcionC': forms.TextInput(attrs={'class': 'form-control'}),
            'opcionD': forms.TextInput(attrs={'class': 'form-control'}),
            'correcta': forms.Select(attrs={'class': 'form-control'}),
        }

        

PreguntaFormSet = inlineformset_factory(Test, Pregunta, form=PreguntaForm, can_delete=True, extra=1, min_num=1, validate_min=True )

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo', max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Correo'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError("Correo o contraseña incorrectos.")
        return self.cleaned_data

