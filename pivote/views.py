from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "pivote/home.html")

def login(request):
    if request.method == "POST":
        contraseña = request.POST.get("contraseña")
        mail = request.POST.get("mail")

        if "@" in mail:
            mail = mail
        else:
            try:
                nombre = mail
                user = Usuario.objects.get(nombre=nombre)
                mail = user.mail
            except Usuario.DoesNotExist:
                mail = "ERR-01"



        try:
            usuario_selec = Usuario.objects.get(mail=mail)
            if(str(contraseña) == str(usuario_selec.password) and mail != "ERR-01"):
                datos={}
                datos["nombre"]=usuario_selec.nombre
                return render(request, 'pivote/initial.html',datos)
            else:
                messages.error(request, "ERROR: Contraseña incorrecta, por favor vuelva a intentarlo.")
                return render(request, 'pivote/home.html')
        except Usuario.DoesNotExist:
            messages.error(request, "ERROR: Cuenta no existente, por favor vuelva a intentarlo.")
            return render(request, 'pivote/home.html')