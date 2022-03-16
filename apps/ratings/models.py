from django.contrib.auth.models import User
from django.db import models


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    rating = models.IntegerField(verbose_name='Nota')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
