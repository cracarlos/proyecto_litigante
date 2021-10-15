from django.db import models

class Diligencias(models.Model):
	cliente = models.CharField(max_length=50, null=False)
	ci = models.CharField(max_length=9, null=False)
	fecha = models.DateField(null=False)
	cualidad = models.CharField(max_length=40, null=False)
	delitos = models.CharField(max_length=40, null=False)
	contraparte = models.CharField(max_length=40, null=False)
	k = models.CharField(max_length=40, null=False)
	or_policial = models.CharField(max_length=40, null=False)
	direccion_reclusion = models.CharField(max_length=40, null=False)
	juzgado = models.CharField(max_length=40, null=False)
	secretario = models.CharField(max_length=40, null=False)
	fiscalia = models.CharField(max_length=40, null=False)
	ubicacion = models.CharField(max_length=200, null=False)
	fiscal = models.CharField(max_length=80, null=False)
	mp = models.CharField(max_length=80, null=False)
	causa = models.CharField(max_length=80, null=False)
	pronunciamiento = models.CharField(max_length=80, null=False)
	sala = models.CharField(max_length=80, null=False)
	decision = models.CharField(max_length=80, null=False)
	juez = models.CharField(max_length=80, null=False)
	ejecucion = models.CharField(max_length=80, null=False)
	amparo = models.CharField(max_length=80, null=False)
	casacion = models.CharField(max_length=80, null=False)
	creado_el = models.DateTimeField(auto_now_add=True)
	modificado_el = models.DateTimeField(auto_now=True)