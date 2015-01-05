from django.db import models

# Create your models here.

class Rol(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField()
	#id_permiso = models.ManyToManyField('permisos.Permisos', blank=True, related_name= 'tienePermiso')	



