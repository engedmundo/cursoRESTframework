from django.db import models


class Benefit(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    opening_hours = models.TextField(verbose_name="Horário de funcionamento")
    minimum_age = models.IntegerField(verbose_name="Idade mínima")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
