from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, TestForm, PreguntaFormSet
from .models import Test, Pregunta
from django.core.mail import send_mail
from django.conf import settings

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