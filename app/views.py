from email.headerregistry import Group
from tokenize import group
import requests

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q

# Create your views here.
#    #    #    #    # INICIO SESION     #   #   #
def index(request):
    return render(request, 'app/index.html')

def base(request):
    return render(request,'app/base.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def iniciarsesion(request):
    return render(request, 'app/iniciar-sesion.html')

def quienessomos(request):
    return render(request, 'app/quienes-somos.html')

@login_required
def suscripcion(request):
    suscripcionAll = Suscripcion.objects.all()
    datos = {
        'suscripciones' : suscripcionAll
    }
    if request.method == 'POST':
        usuarios = Suscripcion()
        usuarios.usuario = request.user.get_username()
        usuarios.suscrito = request.POST.get('estado')
        usuarios.save()
    return render(request, 'app/suscripcion.html',datos)

def registrarse(request):
    return render(request, 'app/registrarse.html')


#   #   #   AGREGAR,MODIFICAR Y ELIMINAR PRODUCTOS

def agregar(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
        else:
          messages.success(request,'Codigo ya registrado, intente con uno diferente.')
    

    return render(request,'app/productos/agregar.html', datos)

def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            datos['form'] = formulario
    return render(request,'app/productos/modificar.html', datos)


def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/productos/listar.html',datos)


def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to="listar")

#   #   #   #   CARRITO     #   # -> El benja lo dijo e.e
@login_required
def carritocompras(request):
    carritocomprasAll = Carrito.objects.all()
    suscripcionAll = Suscripcion.objects.all()
    total = 0
    totaldescuento = 0
    desc = 0
    for i in carritocomprasAll: 
        if request.user.get_username() in i.usuario:
         total += i.precio * i.cantidad
         totaldescuento += (i.precio * i.cantidad) * 0.95
         desc = total - totaldescuento
    datos = { 'listaCarrito' : carritocomprasAll, 'total' : total, 'totaldescuento' : totaldescuento , 'suscripciones' : suscripcionAll, 'desc' : desc}
    if request.method == 'POST':
        productos = Carrito()
        productos.id = request.POST.get('id')
        prod = productos.delete()
        if prod[0] == 0:
            codigop = request.POST.get('codigop')
            stock = request.POST.get('stocks')
            producto = Producto.objects.get(codigo=int(codigop))
            producto.stock += int(stock)
            producto.save()
    return render(request, 'app/mi-cuenta/carrito-compras.html', datos)

#   #   #   #   #   MENU INICIO DE SESION #     #    #
@login_required
def finalizarcompra(request):
    productosAll = Carrito.objects.all()
    historialAll = Historial.objects.all()
    suscripcionAll = Suscripcion.objects.all()
    total = 0
    totaldescuento = 0
    desc = 0
    for i in productosAll:
        if request.user.get_username() in i.usuario:
          total += i.precio * i.cantidad
          totaldescuento += (i.precio * i.cantidad) * 0.95
          desc = total - totaldescuento
    datos = {'total' : total, 'totaldescuento' : totaldescuento,'desc': desc, 'suscripciones': suscripcionAll}
    norden = 1
    for i in historialAll:
        if request.user.get_username() in i.usuario:
            norden += 1
    if total > 0:
     if request.method == 'POST':
        for i in productosAll:
            carritoHistorico = HistorialCarrito()
            carritoHistorico.usuario = request.user.get_username()
            carritoHistorico.codigo = i.codigo
            carritoHistorico.cantidad = i.cantidad
            carritoHistorico.nombre = i.nombre
            carritoHistorico.precio = i.precio
            carritoHistorico.imagen = i.imagen
            carritoHistorico.orden = norden
            carritoHistorico.save()

        historial = Historial()
        historial.orden = norden
        historial.usuario = request.user.get_username()
        historial.preciototal = total
        historial.estado = Seguimiento.objects.get(codigo=1)
        historial.save()
        productosAll.delete()
    
    return render(request, 'app/mi-cuenta/finalizar.compra.html', datos)
@login_required    
def historialcompras(request):
    historiaAll = Historial.objects.all()
    carritoHistorialAll = HistorialCarrito.objects.all()
    datos = {
        'listaHistorial' : historiaAll,
        'listaCarrito' : carritoHistorialAll
    }
    return render(request, 'app/mi-cuenta/historial-compras.html', datos)

def menuingresado(request):
    return render(request, 'app/mi-cuenta/menu-ingresado.html')

def miscompras(request):
    return render(request, 'app/mi-cuenta/mis-compras.html')

def misdirecciones(request):
    return render(request, 'app/mi-cuenta/mis-direcciones.html')

def modificardatos(request):
    return render(request, 'app/mi-cuenta/modificar-datos.html')

def registro(request):
    return render(request, 'app/mi-cuenta/registro.html')

def seguimiento(request):
    return render(request, 'app/mi-cuenta/seguimiento.html')
    
   #   #   #   #   productos
@login_required
def flores(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        prod = Carrito()
        codigoprod = request.POST.get('codigop')
        stock = request.POST.get('stocks')
        precio = request.POST.get('precio')
        usuarioprod = request.POST.get('txtUsuario')
        imagen = request.POST.get('imagen')
        nombre = request.POST.get('nombre')
        if Carrito.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre)).exists(): 
            product = Carrito.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            prod.codigo = request.POST.get('codigop')
            prod.nombre = request.POST.get('nombre')
            prod.precio = int(stock) * int(precio)
            prod.imagen = request.POST.get('imagen')
            prod.cantidad = request.POST.get('stocks')
            prod.usuario = request.POST.get('txtUsuario')
            prod.save()
        stocks = request.POST.get('stocks')
        codigop = request.POST.get('codigop')
        producto = Producto.objects.get(codigo=int(codigop))
        producto.stock -= int(stocks)
        producto.save()



    return render(request, 'app/tienda/flores.html',datos)

@login_required
def maceteros(request):
    productosAll = Producto.objects.all()
    
    datos = {
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        codigoprod = request.POST.get('codigop')
        stock = request.POST.get('stocks')
        precio = request.POST.get('precio')
        usuarioprod = request.POST.get('txtUsuario')
        imagen = request.POST.get('imagen')
        nombre = request.POST.get('nombre')
        if Carrito.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre)).exists(): 
            product = Carrito.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            prod.codigo = request.POST.get('codigop')
            prod.nombre = request.POST.get('nombre')
            prod.precio = int(stock) * int(precio)
            prod.imagen = request.POST.get('imagen')
            prod.cantidad = request.POST.get('stocks')
            prod.usuario = request.POST.get('txtUsuario')
            prod.save()
        stocks = request.POST.get('stocks')
        codigop = request.POST.get('codigop')
        producto = Producto.objects.get(codigo=int(codigop))
        producto.stock -= int(stocks)
        producto.save()
    
    return render(request, 'app/tienda/maceteros.html',datos)
@login_required
def arbustos(request):
    productosAll = Producto.objects.all()
    datos = { 
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        codigoprod = request.POST.get('codigop')
        stock = request.POST.get('stocks')
        precio = request.POST.get('precio')
        usuarioprod = request.POST.get('txtUsuario')
        imagen = request.POST.get('imagen')
        nombre = request.POST.get('nombre')
        if Carrito.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre)).exists(): 
            product = Carrito.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            prod.codigo = request.POST.get('codigop')
            prod.nombre = request.POST.get('nombre')
            prod.precio = int(stock) * int(precio)
            prod.imagen = request.POST.get('imagen')
            prod.cantidad = request.POST.get('stocks')
            prod.usuario = request.POST.get('txtUsuario')
            prod.save()
        stocks = request.POST.get('stocks')
        codigop = request.POST.get('codigop')
        producto = Producto.objects.get(codigo=int(codigop))
        producto.stock -= int(stocks)
        producto.save()

    return render(request, 'app/tienda/arbustos.html', datos)
@login_required
def tierradehoja(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        prod = Carrito()
        codigoprod = request.POST.get('codigop')
        stock = request.POST.get('stocks')
        precio = request.POST.get('precio')
        usuarioprod = request.POST.get('txtUsuario')
        imagen = request.POST.get('imagen')
        nombre = request.POST.get('nombre')
        if Carrito.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre)).exists(): 
            product = Carrito.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            prod.codigo = request.POST.get('codigop')
            prod.nombre = request.POST.get('nombre')
            prod.precio = int(stock) * int(precio)
            prod.imagen = request.POST.get('imagen')
            prod.cantidad = request.POST.get('stocks')
            prod.usuario = request.POST.get('txtUsuario')
            prod.save()
        stocks = request.POST.get('stocks')
        codigop = request.POST.get('codigop')
        producto = Producto.objects.get(codigo=int(codigop))
        producto.stock -= int(stocks)
        producto.save()

    return render(request, 'app/tienda/tierra-de-hoja.html',datos)



#   #   #   #administrador
@permission_required('app.add_usuario')
def agregarusuario(request):
    datos = {
        'user' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario agregado correctamente!"
        else:
          datos['mensaje'] = "Codigo ya registrado, intente con uno diferente."
    return render(request,'app/usuario/agregar_usuario.html', datos)

@permission_required('app.change_usuario')
def modificarusuario(request, codigo):
    producto = Usuario.objects.get(codigo=codigo)
    datos = {
        'user' : UsuarioForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario modificado correctamente!"
            datos['user'] = formulario
    return render(request,'app/usuario/modificar_usuario.html', datos)

@permission_required('app.view_usuario')
def listarusuario(request):
    UsuariosAll = Usuario.objects.all()
    datos = {
        'listaUsuario' : UsuariosAll
    }
    return render(request,'app/usuario/listar_usuario.html',datos)

@permission_required('app.delete_usuario')
def eliminarusuario(request, codigo):
    producto = Usuario.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarusuario")


@permission_required('app.add_producto')
def productosindex(request):
    return render(request, 'app/productos/productos-index.html')

@permission_required('app.add_usuario')
def usuarioindex(request):
    return render(request, 'app/usuario/usuario_index.html')

@permission_required('app.change_seguimiento')
def seguimientoAdmin(request):
    historiaAll = Historial.objects.all()
    datos = {
        'listaHistorial' : historiaAll
    }
    return render(request, 'app/productos/seguimientoAdmin.html',datos)

@permission_required('app.change_seguimiento')
def modificarSeguimiento(request, orden):
    estado = Historial.objects.get(orden=orden)
    datos = {
        'form' : HistorialForm(instance=estado)
    }
    if request.method == 'POST':
        formulario = HistorialForm(request.POST, files=request.FILES,instance=estado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Seguimiento guardado correctamente!')
            datos['form'] = formulario
    return render(request, 'app/productos/modificarSeguimiento.html',datos)

#login/Registro

def registro_usuario(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            group = Group.objects.get(name='cliente')
            group.user_set.add(usuario)
            suscrito = Suscripcion()
            suscrito.usuario = request.POST.get('username')
            suscrito.suscrito = False
            suscrito.save()
            formulario.save()
            messages.success(request,'Usuario guardado correctamente!')
    return render(request,'registration/registro.html',datos)

#api
@login_required
def api(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    datos = { 
        'listaJson' : response,
    }
    return render(request, 'app/tienda/api.html', datos)

@login_required
def api2(request):
    response = requests.get('https://dbd-api.herokuapp.com/perks').json()
    datos = { 
        'listaDigimon' : response,
    }
    return render(request, 'app/tienda/api2.html',datos)
