from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Provincia, Contacto, Pais

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'provincia', 'pais', 'creado_el')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('provincia', 'pais')

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

admin.site.unregister(Group)
admin.site.unregister(User)