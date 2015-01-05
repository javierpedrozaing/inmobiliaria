from django.db import models
from usuarios.models import Usuarios
from inmuebles.models import Inmuebles

# Create your models here.

class Contratos(models.Model):
	fechaInicial = models.DateField()
	fechaFinal = models.DateField()
	fechaDePago = models.DateField()
	fechaCreacion = models.DateField()
	fechaActualizacion = models.DateField()
	id_usuario = models.ForeignKey(Usuarios, null=True, related_name='id_usuario')	
	
