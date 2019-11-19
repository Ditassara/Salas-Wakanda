from django.db import models
import uuid

# Create your models here.

class Tipo(models.Model):
	name=models.CharField(max_length=200)
	
	def __str__(self):
		return self.name 
		
class Sala(models.Model):
	name=models.CharField(max_length=200)
	tipo=models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)
	valor=models.IntegerField(default=0)
	
	def __str__(self):
		return self.name 
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this room."""
		return reverse('room-detail', args=[str(self.id)])
		
class Arriendo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	fecha_agenda= models.DateTimeField(auto_now=True)
	fecha_inicio= models.DateTimeField(null=True, blank=True)
	fecha_termino= models.DateTimeField(null=True, blank=True)
	sala= models.ForeignKey('Sala', on_delete=models.SET_NULL, null=True)
	banda = models.CharField(max_length=200)
	
	def __str__(self):
		return self.banda 