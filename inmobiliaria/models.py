from django.db import models

class Inmobiliaria(models.Model):
	nombre = models.CharField(max_length=255)
	direccon = models.CharField(max_length=255)
	telefono = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255)
