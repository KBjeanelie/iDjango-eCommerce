from django.contrib.auth.models import User
from django.db import models
from admin_shop.models.product import Product


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


