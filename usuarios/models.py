from django.db import models
from roles.models import Rol

# Create your models here.

class Usuarios(models.Model):
	Nombres = models.CharField(max_length=255)
	Apellidos = models.CharField(max_length=255)
	nombreUsuario = models.CharField(max_length=255)
	password = models.TextField(max_length=255)
	telefono = models.IntegerField()
	direccion = models.TextField()
	email = models.EmailField()
	id_rol = models.ForeignKey(Rol, null=True, related_name='id_rol')




