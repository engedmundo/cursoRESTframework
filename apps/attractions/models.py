from django.db import models

from apps.benefits.models import Benefit
from apps.comments.models import Comment
from apps.locations.models import Location


class Attraction(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    descrption = models.TextField(verbose_name="Descrição")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)
    benefit = models.ManyToManyField(Benefit, verbose_name="Recursos")
    comment = models.ManyToManyField(Comment, verbose_name='Comentário')


"""
    avaliacoes = models.ManyToManyField(Avaliacao)
    foto = models.ImageField(
        upload_to='pontos-turisticos', null=True, blank=True)
"""


def __str__(self):
    return self.name
