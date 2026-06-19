from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "estado", "fecha_creacion", "tiene_imagen")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "autor", "contenido")

    @admin.display(boolean=True, description="Imagen")
    def tiene_imagen(self, obj):
        return bool(obj.imagen)
