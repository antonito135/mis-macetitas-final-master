from django.urls import path, include
from rest_framework import routers
from .views import *

#agrega una ruta en la api

router = routers.DefaultRouter()
router.register(r'producto', ProductoViewSet)
router.register(r'tipoproducto', TipoProductoViewSet)
router.register(r'Suscripcion', SuscripcionViewSet)
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Tipo Usuario', TipousuarioViewSet)
urlpatterns = [
    path('api/', include(router.urls)),




]
