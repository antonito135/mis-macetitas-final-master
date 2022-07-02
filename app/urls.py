from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('productos/agregar',agregar, name="agregar"),
    path('contacto',contacto, name="contacto"),
    path('iniciar-sesion',iniciarsesion, name="iniciarsesion"),
    path('quienes-somos',quienessomos, name="quienessomos"),
    path('registrarse',registrarse, name="registrarse"),
    path('mi-cuenta/suscripcion',suscripcion, name="suscripcion"),
    path('mi-cuenta/carrito-compras',carritocompras, name="carritocompras"),
    path('mi-cuenta/finalizar.compra',finalizarcompra, name="finalizarcompra"),
    path('mi-cuenta/historial-compras',historialcompras, name="historialcompras"),
    path('mi-cuenta/seguimiento',seguimiento, name="seguimiento"),
    path('mi-cuenta/menu-ingresado',menuingresado, name="menuingresado"),
    path('mi-cuenta/mis-compras',miscompras, name="miscompras"),
    path('mi-cuenta/mis-direcciones',misdirecciones, name="miscompras"),
    path('mi-cuenta/modificar-datos',modificardatos, name="modificardatos"),
    path('mi-cuenta/registro',registro, name="registro"),
    path('tienda/arbustos',arbustos, name="arbustos"),
    path('tienda/flores',flores, name="flores"),
    path('tienda/maceteros',maceteros, name="maceteros"),
    path('tienda/tierra-de-hoja',tierradehoja, name="tierradehoja"),

    path('productos/modificar/<codigo>/',modificar, name="modificar"),
    path('productos/eliminar/<codigo>/',eliminar, name="eliminar"),
    path('productos/listar',listar, name="listar"),
    path('productos/productos-index',productosindex, name="productosindex"),
    path('productos/seguimientoAdmin',seguimientoAdmin, name="seguimientoAdmin"),
    path('productos/modificarSeguimiento/<orden>/',modificarSeguimiento, name="modificarSeguimiento"),

    path('usuario/agregar_usuario',agregarusuario, name="agregarusuario"),
    path('usuario/listar_usuario',listarusuario, name="listarusuario"),
    path('usuario/modificar_usuario/<codigo>/',modificarusuario, name="modificarusuario"),
    path('usuario/eliminar_usuario/<codigo>/',eliminarusuario, name="eliminarusuario"),
    path('usuario/usuario_index',usuarioindex, name="usuarioindex"),

    path('registration/registro',registro_usuario, name="registro_usuario"),
    

        #api
    path('tienda/api',api, name="api"),
    path('tienda/api2',api2, name="api2"),

]