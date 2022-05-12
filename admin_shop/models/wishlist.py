from django.db import models
from admin_shop.models.product import Product
from eCommerce.settings import User


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return 'Wish list of ' + str(self.user)


