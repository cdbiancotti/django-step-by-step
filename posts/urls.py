from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("posts/nuevo/", views.post_crear, name="crear"),
    path("posts/<int:pk>/", views.post_detalle, name="detalle"),
    path("posts/<int:pk>/editar/", views.post_editar, name="editar"),
    path("posts/<int:pk>/eliminar/", views.post_eliminar, name="eliminar"),
]
