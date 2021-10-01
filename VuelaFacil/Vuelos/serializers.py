
from rest_framework import  serializers
from Vuelos.models import *
class AeropuertoSerial(serializers.ModelSerializer):

    class Meta:
        model=Aeropuerto
        fields="__all__"

class AvionSerial(serializers.ModelSerializer):

    class Meta:
        model=Avion
        fields="__all__"

class TipoVueloSerial(serializers.ModelSerializer):

    class Meta:
        model=TipoVuelo
        fields="__all__"