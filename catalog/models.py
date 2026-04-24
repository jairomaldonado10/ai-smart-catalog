from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    description = models.TextField(verbose_name="Descripción detallada")
    price = models.IntegerField(verbose_name="Precio en CLP")
    category = models.CharField(max_length=100, verbose_name="Categoría")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - ${self.price}"