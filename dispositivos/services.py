import json
from django.conf import settings


def _cargar_json(nombre_archivo):
    ruta = settings.BASE_DIR / "data" / nombre_archivo
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError(f"Se esperaba una lista en {nombre_archivo}")
    return datos


def cargar_zonas():
    return _cargar_json("zonas.json")


def cargar_categorias():
    return _cargar_json("categorias.json")


def cargar_dispositivos():
    return _cargar_json("dispositivos.json")