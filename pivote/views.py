from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm

def home(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pivote/home.html', {'form': form, 'message': '¡Usuario registrado correctamente!'})
    else:
        form = UserRegistrationForm()
    return render(request, 'pivote/home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pivote/home.html', {'form': form, 'message': 'Registro exitoso, por favor verifica tu correo'})
    else:
        form = UserRegistrationForm()
    return render(request, 'pivote/home.html', {'form': form})


def acceso(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')  # Cambia 'main_page' por el nombre de tu vista principal
            else:
                return render(request, 'pivote/acceso.html', {'form': form, 'message': 'Correo o contraseña incorrectos.'})
    else:
        form = LoginForm()
    return render(request, 'pivote/acceso.html', {'form': form})


def main_page(request):
    # Aquí deberías definir la lógica y plantilla para la página principal a la que los usuarios registrados serán redirigidos.
    return render(request, 'pivote/main_page.html')
