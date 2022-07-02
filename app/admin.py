from re import search
from django.contrib import admin
from .models import *
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen']
    search_fields = ['codigo']
    list_per_page = 10

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','apellido','email','password','tipo_usuario']
    search_fields = ['nombre']
    list_per_page = 10

admin.site.register(TipoUsuario)
admin.site.register(Usuario, UsuarioAdmin)

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['codigo','estado']
    search_fields = ['codigo']
    list_per_page = 4

admin.site.register(Seguimiento, SeguimientoAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','precio','imagen']
    search_fields = ['nombre']
    list_per_page = 10

admin.site.register(Carrito)

admin.site.register(Suscripcion)

class historialCarritoadmin(admin.ModelAdmin):
    list_display = ['usuario','codigo','cantidad','nombre','precio','imagen', 'orden']
    list_per_page = 10

admin.site.register(HistorialCarrito, historialCarritoadmin )


class historialAdmin(admin.ModelAdmin):
    list_display = ['orden','usuario','preciototal','estado']
    list_per_page = 10

admin.site.register(Historial,historialAdmin )
