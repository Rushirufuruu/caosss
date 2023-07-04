from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name = 'IND'),
    path('galeria', galeria, name = 'GAL'),
    path('inicio_sesion', inicio_sesion, name = 'INI'),
    path('logout', cerrar_sesion,name='LOGOUT'),
    path('deportes', deportes, name = 'DEP'),
    path('formulario', formulario, name = 'FORM'),
    path('login/',login,name='LOGIN'),
    path('ingresar_noticia', ingresar_noticia, name = 'INGN'),
    path('internacional', internacional, name = 'INT'),
    path('nacional', nacional, name = 'NAC'),
    path('politica', politica, name = 'POL'),
    path('perfil_periodista', perfil_periodista, name= 'PFP'),
    path('noticias/', noticias, name= 'NOTI'),
    path('search_noticias', views.SearchNoticias.as_view(), name = 'search_noticias'),
    path('productos', productos, name= 'PROD'),
    path('carrito', carrito, name= 'CAR'),
    path('agregar_carrito/<id_producto>/',agregar_carrito, name = 'AC' ),
    path('restar_carrito/<id_producto>/',restar_carrito, name = 'RC' ),
    path('eliminar_carrito/<id_producto>/',eliminar_carrito, name = 'EC' ),
    path('vaciar',vaciar, name = 'VACIAR' ),
    path('eliminar_noticia/<id>/',eliminar_noticia, name = 'EN' ),
    path('modificar/<id>/',modificar, name = 'MOD' ),
    path('editar_noticia',editar_noticia, name = 'EDN' ),
    path('agregar_imagen',agregar_imagen, name = 'AI' ),
    path('galeria_noti/<id>/',galeria_noti, name = 'GNT' ),

]