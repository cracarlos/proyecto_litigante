from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UserAdminModificado(UserAdmin):
    fieldsets = ()
    add_fieldsets = (
        (None,{
            'fields': ('email','password1','password2','usuario','is_superuser',),
        }),
    )

    list_display = ('email','is_staff','is_superuser','is_active',)
    search_fields = ('usuario','email',)
    ordering = ('usuario',)

admin.site.site_header = 'Administración de Kraken'

admin.site.register(Usuario, UserAdminModificado)
