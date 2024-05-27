from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request, "pivote/home.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(request, username=username,password = password)
        print(user)
        if user is not None:
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