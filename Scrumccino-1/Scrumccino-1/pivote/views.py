from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import LoginForm
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request, "pivote/home.html")

def login(request):
    title = "Login"
    
    if request.method == 'GET':
        
        if request.user.is_authenticated:
            return redirect(inicio)

        form = LoginForm()

        data = {
            'title': title,
            'form': form,
        }
        return render(request,'pivote/login.html', data)
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user = authenticate(email=email,password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request,f'Hola {email.title()}, bienvenido!')
                return redirect(inicio)
            else:
                _, domain = email.split('@')
                _, com= domain.split('.')
                if '@' not in email:
                    messages.error(request,f'El correo no contiene "@"')
                    return redirect(home)
                if '.' not in domain or com==None:
                    messages.error(request,f'El correo no presenta dominio')
                    return redirect(home)
                else:
                    messages.error(request,f'Usuario o contrasena invalida')
                    return redirect(home)
                
        data = {
            'title' : title,
            'form': form
        }
    return render(request, "pivote/inicio.html")

def inicio(request):
    return render (request, "pivote/inicio.html")

def logout(request):
    messages.success(request,f'Has cerrado sesion')
    return render(request, "pivote/logout.html")

