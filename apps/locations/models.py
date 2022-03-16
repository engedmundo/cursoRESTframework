from django.db import models


class Location(models.Model):
    line1 = models.CharField(max_length=150, verbose_name='Endereço')
    line2 = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name='Complemento endereço')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
    country = models.CharField(max_length=50, verbose_name='País')
    latitude = models.IntegerField(
        blank=True, null=True, verbose_name='Latitude')
    longitude = models.IntegerField(
        blank=True, null=True, verbose_name='Longitude')

    def __str__(self):
        return self.line1

    class Meta:
        ordering = ["city", ]
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
