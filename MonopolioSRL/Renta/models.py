from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Oficina(models.Model):
    telefono_choice = (('Si','Si'),('No','No'))
    bañoprivado_choice=(('Si','Si'),('No','No'))
    wifi_choice=(('Si','Si'),('No','No'))
    nombre = models.CharField(max_length=200)
    codigo_interno = models.CharField(max_length=100)
    persona_encargada = models.CharField(max_length=200)
    cantidad_personas = models.IntegerField()
    telefono = models.CharField(max_length =200,choices = telefono_choice,default="Si")
    baño_privado = models.Chtelefono = models.CharField(max_length =200,choices = bañoprivado_choice,default ="Si")
    wifi = models.Chtelefono = models.CharField(max_length =200,choices = wifi_choice,default = "Si")
    class Meta:
        verbose_name = "Oficina"
        
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    oficina = models.ForeignKey(Oficina,on_delete=CASCADE)
    nombre_cliente = models.CharField(max_length=200)
    nombre_reserva = models.CharField(max_length=200)
    fecha_reserva = models.DateTimeField(auto_now=True)
    fecha_comienzo = models.DateField()
    fecha_fin = models.DateField()
    class Meta:
        verbose_name = "Reserva"
        
    def __str__(self):
        return str(self.nombre_cliente)