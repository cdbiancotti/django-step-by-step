# Blog Django

Proyecto base de un blog web desarrollado con Django, ahora con navegacion, templates HTML y CSS propio.

## Descripcion

Este repositorio contiene una primera version visual del blog.
Incluye la configuracion base del proyecto, una aplicacion llamada `posts`, una pagina de inicio, una pagina "Acerca de" y estilos cargados desde archivos estaticos.

## Instalacion

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd contenido
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Activar el entorno virtual en Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir en el navegador:

`http://127.0.0.1:8000/`

## Aplicacion principal

- `posts`: aplicacion inicial para manejar las publicaciones del blog.

## Paginas disponibles

- `/`: pagina de inicio del blog.
- `/acerca/`: pagina con informacion del autor y el objetivo del sitio.
