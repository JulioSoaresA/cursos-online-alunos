from django.contrib import admin
from .models import Cursos, Componente, Matriculado


class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'idade_minima')
    list_display_links = ('nome', )
    list_filter = ('nome', 'descricao')
    readonly_fields = ('matriculados', )
    filter_horizontal = ()
    fieldsets = ()


class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nome_componente', 'carga_horaria', )
    list_display_links = ('nome_componente', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MatriculadoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', )
    readonly_fields = ('nome_completo', 'cpf', )

admin.site.register(Cursos, CursosAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Matriculado, MatriculadoAdmin)
