from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

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
        return self.autor.name +" "+ self.asignatura.name + " " +self.titulo + " " + str(self.fecha)


