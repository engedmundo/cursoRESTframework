from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    comment = models.TextField(verbose_name='Comentário')
    data = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username
