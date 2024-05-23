from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    mail = models.CharField(max_length=35, unique=True)
    password = models.CharField(max_length=35)

    def __str__(self):
        m2= ""
        for letra in self.mail:
            if (letra!="@"):
                m2+=letra
            else:
                break
        return m2