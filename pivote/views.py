from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import *

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

def crearPost(request):
    if request.method == "POST":
        print(request.user)
        nuevo_post = Post.objects.create(
            asignatura = Asignatura.objects.get(name=request.POST.get("asignatura")),
            titulo = request.POST.get("titulo"),
            autor = User.objects.get(name=request.user),
            contenido = request.POST.get("contenido")


        )
    data = {}
    asignaturas = Asignatura.objects.all()
    data["asignaturas"] = asignaturas
    return render(request, "pivote/crearPost.html", data)