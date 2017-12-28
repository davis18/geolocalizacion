from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Direccion(models.Model):

    via          = models.CharField(max_length=80)
    urbanizacion = models.CharField(max_length=80)
    distrito     = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return self.distrito