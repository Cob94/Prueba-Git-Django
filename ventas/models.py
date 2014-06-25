from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombre_Completo= "%s %s" % (self.nombre,self.apellidos,)
		return nombre_Completo

class Producto(models.Model):
	def url(self,filename):
		ruta='MultimediaData/Productos/%s/%s' %(self.nombre,str(filename))
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	status= models.BooleanField(default=True)
	imagen= models.ImageField(upload_to=url,null=True,blank=True)
	precio=models.DecimalField(max_digits=6, decimal_places=2)
	stock=models.IntegerField()
	def __unicode__(self):
		return self.nombre