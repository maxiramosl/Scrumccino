from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm  
from django.contrib.auth import authenticate, login

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def home(request):

    return render(request, "pivote/home.html")

@login_required
def plataforma(request):
    return render(request, 'pivote/plataforma.html')

def exit(request):
    logout(request)
    return redirect('home')

def send_email(email):
    context = {'email': email}
    template = get_template('pivote/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Titulo correo',
        'Menaje',
        settings.EMAIL_HOST_USER,
        [email]
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(data = request.POST)  
        if form.is_valid(): 
            email = request.POST.get('email')
            send_email(email) 
            form.save()  
            return redirect('home')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/register.html', context)  
