from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def home(request):

    return render(request, "pivote/home.html")


def send_email(email):

    context = {'email': email
               }
    template = get_template('pivote/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de validación',
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.attach_alternative(content, 'text/html')
    email.send()


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email,password = password)

        print(email)
        if user is not None:
            send_email(email)
            login(request,user)
            messages.success(request,("Has ingresado correctamente")) 
            return redirect('home')

        else:
            messages.success(request,("Cuenta no existente"))
            return redirect('login')
    else:
        return render(request, 'pivote/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("Has salido de tu cuenta"))
    return redirect('home')