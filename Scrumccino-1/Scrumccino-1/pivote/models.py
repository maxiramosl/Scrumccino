from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    correo=models.CharField(max_length=100, blank=False)
    contraseña=models.CharField(max_length=100, )


# Create your models here.
