from django.contrib import admin
from .models import Cliente
from .forms import Cliente


# Register your models here.

admin.site.register(Cliente)

class DropdownModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Tipo Pers', {
            'fields': ('tipo_pers', ('razon_social'))
        }),
    )
    form = Cliente

