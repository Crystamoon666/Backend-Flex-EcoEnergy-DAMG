# Backend-Flex-EcoEnergy-DAMG

Back End del proyecto **EcoEnergy**, desarrollado con Python y Django siguiendo el patrón MVT.

## Descripción y objetivo

EcoEnergy es una aplicación de monitoreo energético que permite consultar zonas de
consumo y los dispositivos instalados en cada una. El proyecto carga sus datos desde
archivos JSON (`data/zonas.json`, `data/categorias.json`, `data/dispositivos.json`),
los relaciona en Python y presenta los resultados mediante plantillas Django con
Bootstrap.

El objetivo es que la aplicación se mantenga funcional al variar la cantidad de
registros (zonas, categorías o dispositivos) sin requerir cambios manuales en las
Vistas o los Templates por cada elemento agregado.

## Requisitos previos

- Python 3.12 o superior (Django 6.1 requiere Python 3.12+).
- `pip` (incluido con Python).
- `git`.
- Un entorno macOS/Linux o Windows con acceso a terminal.

## Clonación del repositorio

```bash
git clone https://github.com/Crystamoon666/Backend-Flex-EcoEnergy-DAMG.git
cd Backend-Flex-EcoEnergy-DAMG
```

## Creación y activación de `.venv`

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
```

Activación del entorno virtual:

- macOS / Linux:

  ```bash
  source .venv/bin/activate
  ```

- Windows (PowerShell):

  ```powershell
  .venv\Scripts\activate
  ```

Al activarse, el prompt de la terminal mostrará el prefijo `(.venv)`.

## Instalación desde `requirements.txt`

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Dependencias del proyecto:

- `Django==6.1`
- `asgiref==3.12.1`
- `django-bootstrap5==26.2`
- `sqlparse==0.6.0`
- `tzdata==2026.3`

## Comandos de verificación

Con el entorno virtual activado y desde la raíz del proyecto:

```bash
python manage.py check
```

Para ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor se levanta en `http://127.0.0.1:8000/`.

## Estado actual y próximos pasos

- **Estado actual:** el entorno se configura con los pasos anteriores y el proyecto
  ejecuta sin errores (`python manage.py check` no reporta problemas). La app
  `dispositivos` ya cuenta con datos de origen en `data/` (zonas, categorías y
  dispositivos) y rutas Django funcionales.
- **Próximos pasos:** continuar con el desarrollo de las funcionalidades solicitadas
  en las siguientes etapas de la asignatura.

## Estructura del proyecto

```
Backend-Flex-EcoEnergy-DAMG/
├── config/                 # Proyecto Django (settings, urls, asgi, wsgi)
├── data/                   # Fuentes de datos JSON (zonas, categorías, dispositivos)
├── dispositivos/           # App Django: urls.py, views.py, services.py, models.py
├── templates/              # Plantillas Django (base.html y templates/dispositivos/)
├── manage.py                # Utilidad de administración de Django
├── requirements.txt         # Dependencias del proyecto
└── .gitignore                # Exclusiones de control de versiones
```
