from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse(
        "<h1>EcoEnergy</h1>"
        "<p>Back End en funcionamiento</p>"
    )


def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )

def personaje_id(request, personaje_id):
    if personaje_id >=15:
        return  HttpResponse(
            f"Personaje encontrado {personaje_id}", status=200
        )
    return HttpResponse(
        f"Dispositivo no encontrado", status=404
    ) 

