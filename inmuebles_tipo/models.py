from django.db import models

from tipoInmueble.models import tipoInmueble
from inmuebles.models import Inmuebles

# Create your models here.

class inmueblesTipo(models.Model):
	#deve tener foreingkey de inmueble y de tipo Inmueble
	tipo = models.ForeignKey(tipoInmueble,null=True, related_name='tipo')
	inmueble = models.ForeignKey(Inmuebles,null=True, related_name='inmueble')
	valorVenta = models.IntegerField()
	ValorArriendo = models.IntegerField()
	fechaArriendo = models.DateTimeField()
	fechaVenta = models.DateTimeField()
