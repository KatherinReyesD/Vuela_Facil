from django.db import models
from django.db.models.fields import CharField
from django.db.models.lookups import PostgresOperatorLookup

# Create your models here.

class Aeropuerto (models.Model):
    Id=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=200)
    Ciudad=models.CharField(max_length=200)
    Disponibilidad=models.BooleanField(True)
    norte=models.FloatField(default=0)
    este=models.FloatField(default=0)

    def __str__(self):
        return self.Nombre

class Avion (models.Model):
    Id = models.CharField(max_length=100,primary_key=True)
    Disponibilidad=models.BooleanField(True)
    NumSillasEco=models.IntegerField(default=0)
    NumSillasEje=models.IntegerField(default=0)
    PesoBodega=models.FloatField(default=0)

    UbicacionInicial=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE)

    def sillasDisponiblesEco(self,numeroVendidas):
        return self.NumSillasEco - numeroVendidas

    def sillasDisponiblesEje(self,numeroVendidas):
        return self.NumSillasEje - numeroVendidas

    def pesoDisponible(self,pesovendido):
        return self.PesoBodega - pesovendido


class TipoVuelo(models.Model):

    Tipo=models.CharField(max_length=200)
    AeroSalida=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE,related_name='+')
    AeroLlegada=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE,related_name='+')
    id_Avion=models.ForeignKey(Avion,on_delete=models.CASCADE)
    NumSillasEcoVendidas=models.IntegerField(default=0)
    NumSillasEjeVendidas=models.IntegerField(default=0)
    Peso=models.FloatField(default=0)
    Fecha=models.DateTimeField()
    NumeroSillasVendidas=models.IntegerField(default=0)

    def sillasVendidasEco(self):
        return self.id_Avion.sillasDisponiblesEco(self.NumSillasEcoVendidas)

    def sillasVendidasEje(self,):
        return self.id_Avion.sillasDisponiblesEje(self.NumeroSillasVendidas)

    def pesoOcupado(self):
        return self.id_Avion.pesoDisponible(self.Peso)

    def __str__(self):
        return self.Tipo
    
