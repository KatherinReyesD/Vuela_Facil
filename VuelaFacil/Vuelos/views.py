from rest_framework import viewsets
from Vuelos.serializers import *

class AeropuertoAPI (viewsets.ModelViewSet):
    
    serializer_class=AeropuertoSerial
    queryset = Aeropuerto.objects.all()


class AvionAPI (viewsets.ModelViewSet):
    
    serializer_class=AvionSerial
    queryset = Avion.objects.all()
    

class TipoVueloAPI (viewsets.ModelViewSet):
    
    serializer_class=TipoVueloSerial
    queryset = TipoVuelo.objects.all()
    