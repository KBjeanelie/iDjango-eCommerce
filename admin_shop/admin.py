from django.contrib import admin
from admin_shop.models import Marque, Produit, Cart, WhistListCart, City, Country, Profile

# Register your models here.

admin.site.register(Marque)
admin.site.register(Produit)
admin.site.register(Cart)
admin.site.register(WhistListCart)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Profile)

