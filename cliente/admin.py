from django.contrib import admin
from cliente.models import Cliente

# Register your models here.
@admin.register(Cliente)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20