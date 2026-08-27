from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render

from .services import cargar_zonas, cargar_categorias, cargar_dispositivos


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(request, "dispositivos/inicio.html", contexto)


def listado_zonas(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    resumen_zonas = []
    for zona in zonas:
        cantidad = sum(1 for d in dispositivos if d["zona_id"] == zona["id"])
        resumen_zonas.append({
            "id": zona["id"],
            "nombre": zona["nombre"],
            "limite_kwh": zona["limite_kwh"],
            "cantidad_dispositivos": cantidad,
        })

    return render(request, "dispositivos/zonas.html", {"zonas": resumen_zonas})


def detalle_zona(request, zona_id):
    zonas = cargar_zonas()
    categorias = cargar_categorias()
    dispositivos = cargar_dispositivos()

    zona = next((z for z in zonas if z["id"] == zona_id), None)
    if zona is None:
        raise Http404("Zona no encontrada")

    categorias_por_id = {c["id"]: c["nombre"] for c in categorias}

    dispositivos_zona = [
        {
            "nombre": d["nombre"],
            "categoria": categorias_por_id.get(d["categoria_id"], "Sin categoría"),
            "consumo_kwh": d["consumo_kwh"],
        }
        for d in dispositivos if d["zona_id"] == zona_id
    ]

    consumo_total = sum(d["consumo_kwh"] for d in dispositivos_zona)
    estado = "ALERTA" if consumo_total > zona["limite_kwh"] else "NORMAL"

    contexto = {
        "zona": zona,
        "dispositivos": dispositivos_zona,
        "consumo_total": round(consumo_total, 2),
        "estado": estado,
    }
    return render(request, "dispositivos/detalle_zona.html", contexto)