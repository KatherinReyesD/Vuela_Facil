from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Checkout.views import *

router = DefaultRouter()
router.register('carrito', CarritoAPI )
router.register('tiquete', TiqueteAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]