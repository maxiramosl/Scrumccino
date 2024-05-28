from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

# Create your views here.

def home(request):

    valid = request.GET.get('boton')
    if valid == 'valido':
        return('true')

    return render(request, "pivote/home.html")

@login_required
def plataforma(request):
    
    return render(request, 'pivote/plataforma.html')

def exit(request):
    logout(request)
    return redirect('home')

def send_email(email, name):

    context = {'email': email,
               'name': name,
               }
    template = get_template('pivote/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de validación',
        'Mensaje',
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(data = request.POST)
        
        if form.is_valid() and form.clean_password2 and form.username_clean and form.email_clean: 
            email = request.POST.get('email')
            name = request.POST.get('username')
            send_email(email, name) 
            form.save()  
    else: 
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/register.html', context)