# Blog Django

Proyecto base de un blog web desarrollado con Django, ahora con CRUD completo de posts e imagenes opcionales.

## Descripcion

Este repositorio contiene una version del blog conectada a SQLite y preparada para crear, listar, editar, ver y eliminar publicaciones desde la propia interfaz web.
Incluye la aplicacion `posts`, panel administrativo, carga opcional de imagenes por post y estilos propios.

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

Dependencia nueva para imagenes:

```bash
pip install Pillow
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
- `/posts/nuevo/`: formulario para crear posts.
- `/posts/<id>/`: detalle de cada publicacion.
- `/posts/<id>/editar/`: edicion de publicaciones.
- `/posts/<id>/eliminar/`: confirmacion y borrado.

## CRUD disponible

- Crear posts desde la interfaz web.
- Listar posts en la pagina principal.
- Ver el detalle de cada post.
- Editar publicaciones existentes.
- Eliminar publicaciones con confirmacion previa.

## Manejo de imagenes

- El modelo `Post` usa `ImageField` con `upload_to='posts/'`.
- Django guarda las imagenes en la carpeta `media/posts/`.
- En desarrollo, las imagenes se sirven con `MEDIA_URL` y `MEDIA_ROOT`.
- Para probar la carga, crea o edita un post desde `/posts/nuevo/` y selecciona una imagen antes de guardar.
