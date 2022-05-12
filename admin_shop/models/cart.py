from django.db import models
from admin_shop.models.product import Product
from eCommerce.settings import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    Total_frais = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return 'Cart of ' + str(self.user)

