from django.contrib import admin
from .models import Restaurante, Usuario, Platillo

# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Usuario)
admin.site.register(Platillo)