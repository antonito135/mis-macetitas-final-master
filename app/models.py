
from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo
    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, null=True, blank=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos",null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'db_producto'

class TipoUsuario(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    tipo_usuario = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_usuario

class Usuario(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre
        
class Seguimiento(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado
    class Meta:
        db_table ='db_seguimiento'


class Carrito(models.Model):
    codigo = models.IntegerField()
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to="carrito", null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_items_carrito'


class Suscripcion(models.Model):
    suscrito = models.BooleanField()
    usuario = models.CharField(null=False, primary_key=True,max_length=40)
    def __str__(self):
        return self.usuario


class HistorialCarrito(models.Model):
    usuario = models.CharField(max_length=40)
    codigo = models.IntegerField()
    cantidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="carrito", null=True)
    orden = models.IntegerField()

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = 'db_carrito_historico'


class Historial(models.Model):
    orden = models.IntegerField()
    usuario = models.CharField(max_length=50)
    preciototal = models.IntegerField()
    estado = models.ForeignKey(Seguimiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = 'db_historia'