from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('juegos-formulario/', juegos_formulario, name='juegos-formulario'),
    path('categorias-formulario/', categorias_formulario, name='categorias-formulario'),
    path('lanzamientos-formulario/', lanzamientos_formulario, name='lanzamientos-formulario'),
    path('buscar-juegos/', buscar_juegos, name='buscar-juegos'),
]