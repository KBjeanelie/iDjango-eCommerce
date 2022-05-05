from django.db import models

from admin_shop.models.country import Country


class City(models.Model):
    name_city = models.CharField(max_length=200)
    name_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_city