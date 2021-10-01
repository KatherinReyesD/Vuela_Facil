from django.db import models
from Vuelos.models import TipoVuelo
# Create your models here.

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario
    
    def total(self):
        pass

class Tiquete(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoVuelo, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " - " + self.tipo.__str__()

