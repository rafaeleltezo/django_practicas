from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    contexto = {
        'usuario': 'Osnaider Miranda',
        'ocupacion': 'Programador de lsv'
    }
    return render(request, 'articulos/inicio.html', contexto)


def agregar(request):
    articulos = {
        'nombres':'jabon',
        'etiqueta':'nexo',
        'categoria':'limpieza'
    }
    return render(request,'articulos/agregar.html',articulos)