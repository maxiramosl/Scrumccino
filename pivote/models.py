from django.db import models

class Usuario(models.Model):
    mail = models.CharField(max_length=35)
    password = models.CharField(max_length=35)

    def __str__(self):
        m2= ""
        for letra in self.mail:
            if (letra!="@"):
                m2+=letra
            else:
                break
        return m2