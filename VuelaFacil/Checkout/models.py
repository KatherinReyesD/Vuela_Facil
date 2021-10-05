
from django.db import models
from Usuarios.models import Perfil
from Vuelos.models import TipoVuelo
# Create your models here.

class CarritoCompras(models.Model):
    usuario = models.ForeignKey(Perfil,on_delete=models.SET_NULL,null=True)
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.nombre
    
    def total(self):
        pass

class Tiquete(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoVuelo, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)
    tipoSilla=models.CharField(max_length=50)

    def __str__(self):
        return self.carrito.__str__() + " - " + self.tipo.__str__()

    def CostoTiquete(self):
        dis=((self.tipo.AeroSalida.norte-self.tipo.AeroLlegada.norte)**2+(self.tipo.AeroSalida.este-self.tipo.AeroLlegada.este)**2)**1/2
        if TipoVuelo=="Comercial":
            if self.tipoSilla == "Economica":
                to=(dis*3000)+(self.tipo.Peso*20)
            else:
                to=(dis*5000)+(self.tipo.Peso*40)
        else:
            to=self.tipo.Peso*500*(dis*5000)
        return to         
