from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def home(request):

    return render(request, "pivote/home.html")



def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email,password = password)

        print(email)
        if user is not None:
            send_mail(
            "confirmacion scrumccino",
            "confirmacion de ingreso",
            "scrumccino@gmail.com",
            [email],
            fail_silently=False,)

            
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