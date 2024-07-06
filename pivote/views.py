from django.shortcuts import render
from .models import *

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