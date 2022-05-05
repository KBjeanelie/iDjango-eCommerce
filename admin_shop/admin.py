from django.contrib import admin
from .models import Marque, Produit, Cart, WhistListCart, City, Country, Profile


class AdminMarque(admin.ModelAdmin):
    search_fields= ["label_marque"]
################
class AdminProduit(admin.ModelAdmin):
    list_display=('label','description','date_add','quantity','Prices')
    search_fields = ["label"]
###############
class AdminCity(admin.ModelAdmin):
    list_display = ('name_city','name_count')
    search_fields = ["name_city"]
###############
# Register your models here.


admin.site.register(Marque, AdminMarque)
admin.site.register(Produit, AdminProduit)
admin.site.register(Cart)
admin.site.register(WhistListCart)
admin.site.register(City, AdminCity)
admin.site.register(Country)
admin.site.register(Profile)

