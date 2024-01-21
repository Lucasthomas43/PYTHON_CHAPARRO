from django.contrib import admin

from . import models

admin.site.register(models.Producto)
admin.site.register(models.Zapatilla)
admin.site.register(models.Gorra)
admin.site.register(models.Jean)
admin.site.register(models.Campera)
admin.site.register(models.Usuario)
admin.site.register(models.Vendedor)
admin.site.register(models.Cliente)
admin.site.register(models.Venta)