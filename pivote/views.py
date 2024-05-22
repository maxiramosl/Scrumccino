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
        try:
            usuario_selec = Usuario.objects.get(mail=mail)
            if(str(contraseña) == str(usuario_selec.password)):
                datos={}
                datos["nombre"]=usuario_selec.__str__
                return render(request, 'pivote/initial.html',datos)
            else:
                messages.error(request, "ERROR: Contraseña incorrecta, por favor vuelva a intentarlo.")
                return render(request, 'pivote/home.html')
        except Usuario.DoesNotExist:
            messages.error(request, "ERROR: Cuenta no existente, por favor vuelva a intentarlo.")
            return render(request, 'pivote/home.html')