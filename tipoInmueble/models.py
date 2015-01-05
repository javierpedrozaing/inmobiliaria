from django.db import models

# Create your models here.

class tipoInmueble(models.Model):
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre

