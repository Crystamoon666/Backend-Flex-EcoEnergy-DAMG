# IA.md — Registro de uso de Inteligencia Artificial

## Herramienta utilizada

Claude (Anthropic), interfaz de chat web (claude.ai).
## Mapa de ayuda: en qué parte del código ayudó la IA

| Archivo | Qué existía antes | Ayuda de la IA |
|---|---|---|
| `templates/base.html` | Tenía `{% block content %}` duplicado y dos etiquetas `<body>` (HTML/Template inválido). | Diagnosticó ambos errores y entregó una versión con un solo `<body>` y un solo bloque `content`, dejando `{% bootstrap_javascript %}` antes del cierre del body. |
| `dispositivos/services.py` | Solo tenía `cargar_dispositivos()`, apuntando a un único archivo JSON. | Propuso extenderlo a tres funciones (`cargar_zonas`, `cargar_categorias`, `cargar_dispositivos`) reutilizando una función interna `_cargar_json` para no repetir la lógica de apertura/validación. |
| `dispositivos/views.py` | Tenía dos definiciones de `inicio()` y dos de `catalogo()` (código muerto por duplicado), más `personaje_id()` y `dispositivos_zona()` de otro ejercicio, sin relación con el caso EcoEnergy. | Propuso reemplazar todo por tres vistas: `inicio`, `listado_zonas` (cuenta dispositivos por zona) y `detalle_zona` (cruza zona + categorías + dispositivos, calcula `consumo_total` y el estado NORMAL/ALERTA, y usa `raise Http404` si el id de zona no existe). |
| `dispositivos/urls.py` | Tenía rutas de otros ejercicios (`zonas/<id>/dispositivos/`, `personaje/<id>`, `dispositivos/`). | Propuso dejar solo las tres rutas que pide el enunciado: `""`, `zonas/`, `zonas/<int:zona_id>/`. |
| `templates/dispositivos/zonas.html` | No existía. | Generó el template completo (cards Bootstrap por zona, botón "Ver detalle", estado vacío "No hay zonas disponibles"), siguiendo el Boceto 1 del enunciado. |
| `templates/dispositivos/detalle_zona.html` | No existía. | Generó el template completo (tarjetas de resumen, badge NORMAL/ALERTA con texto e ícono, tabla responsive de dispositivos, estado vacío "Esta zona no tiene dispositivos"), siguiendo el Boceto 2 del enunciado. |
| `templates/dispositivos/catalogo.html` | Era el catálogo de la Clase 5 (no correspondía a la Fase 1). | Recomendó eliminarlo junto con su ruta, ya que el enunciado pide `/zonas/` y `/zonas/<id>/`, no `/dispositivos/`. |


Ejemplo del prompt usado para pedir la actualización del backend:
> "Bien ahora para objetivo de la evaluación debo actualizar en mi repositorio de git [URL] la función en server.py [código] y la función en views.py [código] para finalmente desarrollar el template para que simile a la imagen [boceto adjunto]."

## Cambios propios y verificación

Pruebas:
  - `/zonas/` → Se muestran las tres zonas Norte, Sur y Este, con el limite y la cantidad de dispositivos.
  - `/zonas/1/` (zona con dispositivos) Se muestran los resultados correspondietes.
  - `/zonas/<id inexistente>/` → Se muestra 404
  - Zona sin dispositivos en el JSON, aparece el mensaje "Esta zona no tiene dispositivos."
  - Si paso el limite `consumo_kwh` aparece el mensaje y estado de alerta.

## Interacción 2 — Estructura y contenido de ANALISIS.md

**Prompt utilizado (resumen del original):**
> "Necesito crear un archivo llamado ANALISIS.md que debe contener: relaciones, multiplicidades, claves de conexión y matriz Criterio de aceptación | Archivo/Componente | Prueba.¿Cómo lo puedo armar?"

**Respuesta utilizada:**
Claude clonó el repositorio, revisó `dispositivos/services.py`, `dispositivos/views.py`, `dispositivos/urls.py`, `config/urls.py`, los tres archivos JSON de `data/` y los templates, y propuso una estructura para `ANALISIS.md` con:
- Tabla de entidades (Zona, Categoría, Dispositivo) y sus relaciones.
- Diagrama de relaciones (Mermaid ER).
- Tabla de multiplicidades (1 a 0..N, N a 1) entre Zona–Dispositivo y Categoría–Dispositivo.
- Tabla de claves de conexión (clave primaria lógica `id` en cada JSON; claves foráneas lógicas `zona_id` y `categoria_id` en `dispositivos.json`).
- Matriz de trazabilidad completa, mapeando cada criterio CA-01 a CA-13 del enunciado contra el archivo/función real que lo resuelve (`views.py`, `services.py`, cada template) y la prueba de la sección 6 del enunciado que lo verifica.
