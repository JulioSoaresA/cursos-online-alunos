from django.contrib import admin
from .models import Cursos, Componente, Matriculado, Atividades


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


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome_usuario', 'nome_componente', 'arquivo', 'status', )
    list_display_links = ('nome_usuario',)
    readonly_fields = ('id_usuario', 'nome_usuario', 'nome_componente', 'arquivo', )


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Matriculado, MatriculadoAdmin)
admin.site.register(Atividades, AtividadeAdmin)
