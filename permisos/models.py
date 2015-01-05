from django.db import models
from roles.models import Rol

# Create your models here.

class Permisos(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(max_length=255)
	id_rol= models.ForeignKey(Rol,null=True, related_name='id_roles')
