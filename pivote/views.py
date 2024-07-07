from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,get_user
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.

def home(request):
    usuario=get_user(request)
    usuarioactual="anonimo"
    correoactual="anonimo"
    anonimo=usuario.is_anonymous

    if anonimo == False:
        usuarioactual = usuario.get_username
        
        correoactual = usuario.email 

    
    data={
        "anonimo":anonimo,
        "usuarioactual":usuarioactual,
        "correoactual":correoactual,
    }



    return render(request, "pivote/home.html", data)

def logine(request):
    existe=False
    if request.method=="POST":
        logout(request)
        nombre=request.POST.get("nombre")
        contraseña=request.POST.get("contraseña")
        user = authenticate(request, username=nombre, password=contraseña)
        if user is not None:
            login(request, user)
            existe=True
        else:
            existe=False
            
    data={
        "existe" : existe
    }
    
    return render(request,"pivote/login.html",data)

def registrar(request):
    nombre=""
    correo=""
    contraseña=""

    if request.method=="POST":
        nombre=request.POST.get("nombre")
        correo=request.POST.get("correo")
        contraseña=request.POST.get("contraseña")
        #user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        if (nombre!="" and correo!="" and contraseña !=""):
            NuevoUsuario = User.objects.create_user(username=nombre,email=correo,password=contraseña)
            NuevoUsuario.save
            
            send_mail(
            "confirmacion scrumccino",
            "confirmacion de registro",
            "scrumccino@gmail.com",
            [correo],
            fail_silently=False,)
            
    data={
        "nombre":nombre,
        "correo":correo,
        "contraseña":contraseña
    }

        

    return render(request, "pivote/registrar.html", data)

def salir(request):
    logout(request)
    return redirect('home')

#manage.py:
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mocapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

def crearPost(request):
    if request.method == "POST":
        print(request.user)
        nuevo_post = Post.objects.create(
            asignatura = Asignatura.objects.get(name=request.POST.get("asignatura")),
            titulo = request.POST.get("titulo"),
            autor = request.user,
            contenido = request.POST.get("contenido")
        )
    data = {}
    asignaturas = Asignatura.objects.all()
    data["asignaturas"] = asignaturas
    return render(request, "pivote/crearPost.html", data)
