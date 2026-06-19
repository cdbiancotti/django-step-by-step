# Blog Django

Proyecto base de un blog web desarrollado con Django, ahora con navegacion, templates HTML y CSS propio.

## Descripcion

Este repositorio contiene una primera version visual del blog conectada a una base de datos SQLite.
Incluye la configuracion base del proyecto, una aplicacion llamada `posts`, una pagina de inicio dinamica, una pagina "Acerca de", panel administrativo y estilos cargados desde archivos estaticos.

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

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear un superusuario:

```bash
python manage.py createsuperuser
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
- `/admin/`: panel de administracion para crear y gestionar posts.
