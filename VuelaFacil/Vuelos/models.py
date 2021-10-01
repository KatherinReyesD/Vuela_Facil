from django.db import models
from django.db.models.fields import CharField
from django.db.models.lookups import PostgresOperatorLookup

# Create your models here.

class Aeropuerto (models.Model):
    Id=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=200)
    Ciudad=models.CharField(max_length=200)
    Disponibilidad=models.BooleanField(True)

    def __str__(self) -> str:
        return super().__str__()
    pass

class Avion (models.Model):
    Id = models.CharField(max_length=100,primary_key=True)
    Disponibilidad=models.BooleanField(True)
    NumSillasEco=models.IntegerField(default=0)
    NumSillasEje=models.IntegerField(default=0)
    PesoBodega=models.FloatField(default=0)
    UbicacionInicial=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE)

    def sillasDisponiblesEco():
        return

    def sillasDisponiblesEje():
        return

    def pesoDisponible():
        return

    pass

class TipoVuelo(models.Model):

    Tipo=models.CharField(max_length=200)
    AeroSalida=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE,related_name='+')
    AeroLlegada=models.ForeignKey(Aeropuerto,on_delete=models.CASCADE,related_name='+')
    id_Avion=models.ForeignKey(Avion,on_delete=models.CASCADE)
    Peso=models.FloatField(default=0)
    Fecha=models.DateTimeField()


    def __str__(self) -> str:
        return super().__str__()

    pass

