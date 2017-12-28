from django.contrib import admin
from .models import Direccion
# Register your models here.

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ("via","urbanizacion","distrito",)