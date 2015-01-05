from django.db import models

# Create your models here.

class Proyectos(models.Model):
	Nombre = models.CharField(max_length=255)
	Descripcion = models.TextField()


