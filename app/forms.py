from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#login/registro
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name']


# Creamos un template del formulario


class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=25)
    precio = forms.IntegerField(min_value=400)
    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen']
        


class SuscripcionForm(ModelForm):
    class Meta:
        model = Suscripcion
        fields=['usuario']

class UsuarioForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=20)
    class Meta:
        model = Usuario
        fields = ['codigo','nombre','apellido','email','password','tipo_usuario']
     

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['codigo','nombre','precio','imagen','cantidad']


class HistorialCarritoForm(ModelForm):
    class Meta:
        model = HistorialCarrito
        fields = ['usuario','codigo','nombre','precio','imagen','cantidad']

class HistorialForm(ModelForm):
    class Meta:
        model  = Historial
        fields = ['estado']
        