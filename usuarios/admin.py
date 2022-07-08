from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios


class UsuariosAdmin(UserAdmin):
    list_display = ('nome_completo', 'cpf', 'last_login', 'date_joined', 'is_admin', 'is_staff')
    search_fields = ('nome_completo', 'cpf')
    readonly_fields = ('date_joined', 'last_login', 'password2')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Usuarios, UsuariosAdmin)
