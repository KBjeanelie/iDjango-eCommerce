# Create your models here.
from django.db import models


class Marque(models.Model):
    label_marque = models.CharField(max_length=250)

    def __str__(self):
        return self.label_marque
