'''from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.core.mail import send_mail
from django.conf import settings

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    if user.email:
        allowed_domains = ['gmail.com', 'gmail.cl', 'hotmail.com', 'outlook.com']
        domain = user.email.split('@')[-1]
        if domain in allowed_domains:
            subject = "Inicio de sesión exitoso"
            message = f"Hola {user.name}, has iniciado sesión correctamente."
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)
'''
