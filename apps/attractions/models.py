from tabnanny import verbose

from django.db import models

from apps.benefits.models import Benefit
from apps.comments.models import Comment
from apps.locations.models import Location
from apps.ratings.models import Rating


class Attraction(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True)
    benefit = models.ManyToManyField(Benefit, verbose_name="Recursos")
    comment = models.ManyToManyField(
        Comment,
        verbose_name='Comentário',
        null=True,
        blank=True
    )
    rating = models.ManyToManyField(
        Rating,
        verbose_name='Avaliação',
        null=True,
        blank=True
    )
    foto = models.ImageField(
        upload_to='attractions',
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
