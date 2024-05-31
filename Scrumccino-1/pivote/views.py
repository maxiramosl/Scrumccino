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
    print("cosa cosa cosa")
    
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
        form = LoginForm(data=request.POST)
        print("asdfasdfasdf")
        print(request.POST)
        print(form.errors)
        print(form.is_bound)

        if form.is_valid():
            print("is_valid!!!!!")
            email = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=email,password=password)
            print("user: ",user)
            if user is not None:
                # login(request)
                messages.success(request,f'Hola {email.title()}, bienvenido!')
                return redirect(home)
            elif email is not None:
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

