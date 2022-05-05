from django.contrib import admin

from admin_shop.models import Category
from admin_shop.models.cart import Cart
from admin_shop.models.city import City
from admin_shop.models.country import Country
from admin_shop.models.marque import Marque
from admin_shop.models.product import Product
from admin_shop.models.profile import Profile
from admin_shop.models.wishlist import WishList


class AdminMarque(admin.ModelAdmin):
    search_fields = ["label_marque"]


################
class AdminProduit(admin.ModelAdmin):
    list_display = ('label', 'description', 'date_add', 'quantity', 'prices')
    search_fields = ["label"]


###############
class AdminCity(admin.ModelAdmin):
    list_display = ('name_city', 'name_country')
    search_fields = ["name_city"]


###############
# Register your models here.


admin.site.register(Marque, AdminMarque)
admin.site.register(Product, AdminProduit)
admin.site.register(Cart)
admin.site.register(WishList)
admin.site.register(City, AdminCity)
admin.site.register(Country)
admin.site.register(Profile)
admin.site.register(Category)
