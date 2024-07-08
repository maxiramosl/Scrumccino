from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout,get_user
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import UserRegistrationForm, PreguntaForm, TestForm, PreguntaFormSet



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


def custom_logout(request):
    logout(request)
    messages.success(request, "Se cerró la sesión con éxito.")
    return redirect('home')  # Redirigir a la página de inicio u otra página de tu elección.

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


def crearTest(request):
    if request.method == 'POST':

        test_form = TestForm(request.POST)

        if test_form.is_valid():
            test = test_form.save()
            preguntas_formset = PreguntaFormSet(request.POST, instance=test)
            if preguntas_formset.is_valid():
                preguntas_formset.save()
                
                # send_mail(
                #     'New Test Created',
                #     f'Test "{test.titulo}" has been created.',
                #     settings.EMAIL_HOST_USER,
                #     ['jenifer.castillo2103@gmail.com'],
                #     fail_silently=False,
                # )
                return redirect('verTest', test_id=test.id)
            else:
                print(preguntas_formset.errors)
    else:
        test_form = TestForm()
        preguntas_formset = PreguntaFormSet(queryset=Pregunta.objects.none())

    context = {
        'test_form': test_form,
        'preguntas_formset': preguntas_formset,
    }

    return render(request, 'pivote/crearTest.html', context)

def verTest(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'pivote/verTest.html', {'test': test})

def allTestList(request):
    tests = Test.objects.all()
    return render(request, 'pivote/allTestList.html', {'tests': tests})