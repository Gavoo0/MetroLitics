from django.contrib import admin
from .models import Mantenedor_metro, Mantenedor_bus, Reporte


# Register your models here.
admin.site.register(Mantenedor_metro)
admin.site.register(Mantenedor_bus)
admin.site.register(Reporte)