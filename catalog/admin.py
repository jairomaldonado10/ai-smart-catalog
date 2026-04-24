from django.contrib import admin # Cambia esto
from .models import Product

@admin.register(Product) # Agregamos 'admin.' antes del register
class ProductAdmin(admin.ModelAdmin): # Agregamos 'admin.' antes de ModelAdmin
    list_display = ('name', 'price', 'category', 'stock')
    search_fields = ('name', 'category')