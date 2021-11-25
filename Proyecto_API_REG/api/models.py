from django.db import models

# Create your models here.

class registrar(models.Model):
    usuario=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=10)
    contraseña=models.CharField(max_length=10)
