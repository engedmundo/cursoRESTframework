from django.db import models

from apps.benefits.models import Benefit


class Attraction(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    descrption = models.TextField(verbose_name="Descrição")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")
    benefit = models.ManyToManyField(Benefit, verbose_name="Recursos")


"""
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(
        upload_to='pontos-turisticos', null=True, blank=True)
"""


def __str__(self):
    return self.name
