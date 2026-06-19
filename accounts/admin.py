from django.contrib import admin

from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "tiene_imagen")
    search_fields = ("usuario__username", "usuario__email")

    @admin.display(boolean=True, description="Imagen")
    def tiene_imagen(self, obj):
        return bool(obj.imagen)
