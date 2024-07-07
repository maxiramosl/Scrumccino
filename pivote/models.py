from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

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

