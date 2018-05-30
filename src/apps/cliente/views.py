from django.shortcuts import render

# Create your views here.

def inicio(request):
    cliente={
        "nombre":"rafael",
        "apellido":"barboza",
    }
    return render(request,'cliente/inicio.html',cliente)