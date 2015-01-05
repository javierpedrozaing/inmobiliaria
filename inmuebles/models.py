from django.db import models
from django.db.models import QuerySet
from django.utils.text import slugify
from tipoInmueble.models import tipoInmueble

# Create your models here.


class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        count = 2

        slug = slug_text
        while(model._default_manager.filter(slug=slug).exists()):
            slug = '{0}-{1}'.format(slug_text, count)

        return slug

class Inmuebles(SlugMixin, models.Model):
	titulo = models.CharField(max_length=120, default="Inmuebe")
	codigo = models.IntegerField()
	direccion = models.CharField(max_length=120)
	telefono = models.IntegerField(blank=True, null=True)
	habitaciones = models.IntegerField(blank=True, null=True)
	parqueadero = models.NullBooleanField(blank=True)
	Banos = models.IntegerField(blank=True, null=True)
	pisos = models.IntegerField(blank=True, null=True)
	frente = models.IntegerField(blank=True, null=True)
	fondo = models.IntegerField(blank=True, null=True)
	cocina = models.IntegerField(blank=True, null=True)
	descripcion = models.TextField()
	estado = models.TextField()
	logo = models.ImageField(upload_to='LogoInmueble')
	id_tipoInmueble = models.ForeignKey(tipoInmueble, null=True, related_name='id_tipo')
	slug = models.CharField(max_length=100, blank=True, default='')

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = self.get_slug(self.titulo, Inmuebles)
		super(Inmuebles, self).save(*args, **kwargs)





	
