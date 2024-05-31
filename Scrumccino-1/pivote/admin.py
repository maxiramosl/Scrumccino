from django.contrib import admin
from pivote.models import CustomUser

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("correo","contraseña")

admin.site.register(CustomUser,UsuarioAdmin)
    

# Register your models here.
