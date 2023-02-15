from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppBibliotecaGamer.models import *
from .forms import *

# Create your views here.

def inicio(request):
    juegos = Juego.objects.all()
    print(juegos)
    if juegos:
        return render(request, 'AppBibliotecaGamer/inicio.html', {'juegos': juegos}) 
        # , 'categoria': categoria
    else:
        print('################################################################')

#----------- JUEGOS ----------------------------------------------
def juegos_formulario(request):
    if request.method == 'POST':

        mi_formulario = JuegosFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data #Limpia, saca caracteres html, etc
            juego = Juego(nombre=informacion['nombre'], categoria=informacion['categoria'], valoracion=informacion['valoracion'])
            juego.save()
            return redirect('inicio')

    else:
        mi_formulario = JuegosFormulario()

    return render(request, 'AppBibliotecaGamer/juegos-formulario.html', {'formulario_juegos': mi_formulario, 'nombre': 'Jere'})

#----------- CATEGORIAS ----------------------------------------------
def categorias_formulario(request):
    if request.method == 'POST':

        mi_formulario = CategoriasFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data #Limpia, saca caracteres html, etc
            categoria = Categoria(nombre=informacion['nombre'])
            categoria.save()
            return redirect('inicio')

    else:
        mi_formulario = CategoriasFormulario()

    return render(request, 'AppBibliotecaGamer/categorias-formulario.html', {'formulario_categorias': mi_formulario, 'nombre': 'Jere'})

#----------- LANZAMIENTOS ----------------------------------------------
def lanzamientos_formulario(request):
    if request.method == 'POST':

        mi_formulario = LanzamientosFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data #Limpia, saca caracteres html, etc
            categoria = Lanzamiento(nombre=informacion['nombre'],categoria=informacion['categoria'],fecha_de_lanzamiento=informacion['fecha_de_lanzamiento'])
            categoria.save()
            return redirect('inicio')

    else:
        mi_formulario = LanzamientosFormulario()

    return render(request, 'AppBibliotecaGamer/lanzamientos-formulario.html', {'formulario_lanzamientos': mi_formulario, 'nombre': 'Jere'})

#----------- BUSQUEDA ----------------------------------------------
def buscar_juegos(request):
    if request.GET['juego']:
        juego = request.GET['juego']
        juegos = Juego.objects.filter(nombre__icontains=juego) #Case insensitive

        if juegos:
            return render(request, 'AppBibliotecaGamer/resultados-busqueda.html', {'juegos': juegos, 'juego':juego})

        else:
            respuesta = 'No se encontro esa camada'
    return HttpResponse(respuesta)