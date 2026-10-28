<<<<<<< HEAD
# Práctica: Sitio Web Multipágina con Flask y Bootstrap - Biblioteca Universitaria

## Descripción
Este proyecto consiste en un sitio web para una biblioteca universitaria desarrollado con Python (Flask) y Bootstrap 5. Se implementa la herencia de plantillas y navegación multipágina.

## Elementos Implementados

### 1. Estructura de Archivos
* `server.py`: Punto de entrada de la aplicación. Contiene las 4 rutas de Flask y envía las variables `titulo` y `mensaje` a las plantillas.
* `templates/layout.html`: Plantilla base que contiene la estructura HTML, la referencia a Bootstrap, el menú de navegación y el bloque `{% block content %}`.
* `templates/`: Contiene las 4 vistas hijas que heredan de `layout.html`.

### 2. Uso de Jinja2 y Variables
* Todas las rutas en `server.py` utilizan `render_template()` enviando las variables `titulo` y `mensaje`.
* En los archivos HTML se utilizan etiquetas como `{{ titulo }}` y `{{ mensaje }}` para mostrar la información dinámica.

### 3. Herencia de Plantillas
* Las 4 páginas (`index.html`, `catalogo.html`, `servicios.html`, `contacto.html`) comienzan con `{% extends "layout.html" %}`.
* El contenido particular de cada página se define dentro de `{% block content %}`.

### 4. Navegación con Bootstrap
* Se implementó un menú horizontal con la clase `navbar` de Bootstrap 5.
* Se utilizó un color azul (`bg-primary`) y texto blanco (`navbar-dark`) para diferenciarlo del ejemplo original.
* Los enlaces utilizan `url_for()` para enlazar a las rutas de Flask (ej: `href="{{ url_for('index') }}"`).

### 5. Contenido de las Páginas
* **Inicio:** Información general y horarios.
* **Catálogo:** Categorías de materiales (libros, revistas, tesis, recursos digitales).
* **Servicios:** Préstamo, consulta en sala, acceso digital y orientación.
* **Contacto:** Dirección, correo y horario ficticio.
* Todas las páginas utilizan `container-fluid` para el diseño del contenido.

## Cómo ejecutar el proyecto
1. Instalar Flask: `pip install flask`
2. Ejecutar el servidor: `python server.py`
3. Abrir en el navegador: `http://127.0.0.1:5000`
=======
# Biblioteca UDL ICO - Práctica Flask

Proyecto de sitio web multipágina para una biblioteca universitaria.

## Cómo ejecutar
1. Instalar Flask: `pip install flask`
2. Ejecutar: `python server.py`
3. Abrir en navegador: `http://127.0.0.1:5000/`
>>>>>>> c247f2335d25e1990e6128207bc95206be276469
