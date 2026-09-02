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

def resumen_zona(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    resumen_zonas = []
    total_dispositivos = 0
    consumo_total_general = 0

    for zona in zonas:
        dispositivos_zona = [d for d in dispositivos if d["zona_id"] == zona["id"]]
        cantidad = len(dispositivos_zona)
        consumo_total = sum(d["consumo_kwh"] for d in dispositivos_zona)

        if consumo_total > zona["limite_kwh"]:
            estado = "LÍMITE SUPERADO"
            estado_css = "danger"
        else:
            estado = "DENTRO DEL LÍMITE"
            estado_css = "success"

        resumen_zonas.append({
            "id": zona["id"],
            "nombre": zona["nombre"],
            "cantidad_dispositivos": cantidad,
            "consumo_total": round(consumo_total, 2),
            "limite_kwh": zona["limite_kwh"],
            "estado": estado,
            "estado_css": estado_css,
        })

        total_dispositivos += cantidad
        consumo_total_general += consumo_total

    contexto = {
        "titulo": "Resumen de Consumo por Zona",
        "resumen_zonas": resumen_zonas,
        "total_zonas": len(zonas),
        "total_dispositivos": total_dispositivos,
        "consumo_total_general": round(consumo_total_general, 2),
    }
    return render(request, "dispositivos/resumen_zona.html", contexto)