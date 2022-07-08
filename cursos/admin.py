from django.contrib import admin
from .models import Cursos, Componente


class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'idade_minima')
    list_display_links = ('nome',)
    list_filter = ('nome', 'descricao')


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Componente)