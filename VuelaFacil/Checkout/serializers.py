from rest_framework import serializers
from Checkout.models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = "__all__"

class TiqueteSerial(serializers.ModelSerializer):
    class Meta:
        model = Tiquete
        fields = "__all__"
    