from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,get_user
from django.contrib.auth.models import User

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
        

    data={
        "nombre":nombre,
        "correo":correo,
        "contraseña":contraseña
    }
        

    return render(request, "pivote/registrar.html", data)

def salir(request):
    logout(request)
    return redirect('home')
