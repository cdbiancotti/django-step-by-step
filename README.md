# Blog Django

Blog web desarrollado con Django como entrega final del recorrido de Python + Django. El proyecto integra publicaciones con imagen, autenticacion de usuarios, perfiles y rutas protegidas.

## Tecnologias utilizadas

- Python 3
- Django 6
- SQLite
- Pillow
- HTML
- CSS

## Funcionalidades principales

- CRUD completo de posts desde la interfaz web.
- Imagen opcional para cada publicacion.
- Registro de usuarios.
- Login y logout.
- Perfil de usuario con biografia e imagen.
- Proteccion de rutas sensibles con autenticacion.
- Panel administrativo de Django.

## Instalacion

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd contenido
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activarlo en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Activarlo en Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Puesta en marcha

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear un superusuario si queres probar el admin:

```bash
python manage.py createsuperuser
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

`http://127.0.0.1:8000/`

## Flujo principal para probar

1. Entrar a `/accounts/registro/` y crear una cuenta.
2. Confirmar que despues del registro se redirige a `/accounts/perfil/`.
3. Editar biografia e imagen desde `/accounts/perfil/editar/`.
4. Crear un post desde `/posts/nuevo/`.
5. Ver el detalle, editarlo y eliminarlo.
6. Cerrar sesion y comprobar que crear, editar o borrar posts redirige al login.

## Rutas principales

- `/`: inicio con listado de posts.
- `/acerca/`: pagina informativa.
- `/posts/nuevo/`: crear post.
- `/posts/<id>/`: detalle del post.
- `/posts/<id>/editar/`: editar post.
- `/posts/<id>/eliminar/`: eliminar post.
- `/accounts/login/`: login.
- `/accounts/registro/`: registro.
- `/accounts/perfil/`: perfil autenticado.
- `/accounts/perfil/editar/`: editar perfil.
- `/admin/`: panel administrativo.

## Manejo de imagenes

- `Post.imagen` se guarda en `media/posts/`.
- `Perfil.imagen` se guarda en `media/perfiles/`.
- En desarrollo, Django sirve archivos media con `MEDIA_URL` y `MEDIA_ROOT`.
- Si el repositorio no incluye `media/`, podes recrear contenido subiendo nuevas imagenes desde los formularios.

## Seguridad y archivos locales

- El repositorio no incluye `venv/`, `db.sqlite3`, `media/` ni `.env`.
- Las rutas protegidas son: crear post, editar post, eliminar post, ver perfil y editar perfil.
- El listado y el detalle de posts siguen siendo publicos.

## Tests basicos

Ejecutar pruebas:

```bash
python manage.py test
```

## Autor

- Cristian D. Biancotti
