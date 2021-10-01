from rest_framework import viewsets
from Checkout.serializers import *

class CarritoAPI (viewsets.ModelViewSet):
    serializer_class = CarritoSerial
    queryset = CarritoCompras.objects.all()

class TiqueteAPI(viewsets.ModelViewSet):
    serializer_class = TiqueteSerial
    queryset = Tiquete.objects.all()
    