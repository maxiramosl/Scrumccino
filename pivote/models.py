from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asignatura(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True)
    autor= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    fecha= models.DateField(auto_now=True, null=True, blank=True)
    contenido = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.autor.username +" "+ self.asignatura.name + " " +self.titulo + " " + str(self.fecha)

#Crear Test
class Test(models.Model):
    titulo = models.CharField(max_length=150)
    tema = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    enunciado = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='preguntas')
    opcionA = models.CharField(max_length=200, null=True)
    opcionB = models.CharField(max_length=200, null=True)
    opcionC = models.CharField(max_length=200, null=True)
    opcionD = models.CharField(max_length=200, null=True)
    correcta = models.CharField(max_length=10, choices={('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')}, null=True)
    
    def __str__(self):
        return self.enunciado
