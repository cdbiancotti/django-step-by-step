# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripcion

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuracion base del proyecto y una aplicacion llamada `posts`.

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
