from django.contrib import admin
from .models import Restaurante, Platillo, Precio

# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Platillo)
admin.site.register(Precio)

