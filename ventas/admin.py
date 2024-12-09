from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'telefono']
    search_fields = ['nombre', 'telefono']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio_unitario']
    search_fields = ['nombre']