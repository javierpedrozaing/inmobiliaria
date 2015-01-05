from django.db import models
from inmuebles.models import Inmuebles
# Create your models here.

class Fotos(models.Model):
	id_inmueble = models.ForeignKey(Inmuebles)
	descripcion = models.TextField(blank=True)
	fotoNombre = models.ImageField(upload_to='fotosInmueble')
	fotoType = models.CharField(max_length=255)
	fotoSize = models.PositiveIntegerField()
	fotoUpdate = models.DateField()
