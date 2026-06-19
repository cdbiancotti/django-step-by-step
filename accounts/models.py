from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    biografia = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="perfiles/", null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
