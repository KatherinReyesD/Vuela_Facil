from django.urls import path,include

from rest_framework.routers import DefaultRouter
from Vuelos.views import *

router = DefaultRouter()
router.register("aeropuerto",AeropuertoAPI)
router.register("avion",AvionAPI)
router.register("tipovuelo",TipoVueloAPI)


urlpatterns = [

    path("crud/",include(router.urls))

]

