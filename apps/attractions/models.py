from django.db import models


# Create your models here.
class Attraction(models.Model):
    name = models.CharField(max_length=150)
    descrption = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
