from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from admin_shop.forms.user_auth import UserChangeForm, UserCreationForm
from admin_shop.models import Category
from admin_shop.models.cart import Cart
from admin_shop.models.city import City
from admin_shop.models.country import Country
from admin_shop.models.marque import Marque
from admin_shop.models.product import Product
from admin_shop.models.profile import Profile
from admin_shop.models.wishlist import WishList

User = get_user_model()


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


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


# Register your models here.

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Marque, AdminMarque)
admin.site.register(Product, AdminProduit)
admin.site.register(Cart)
admin.site.register(WishList)
admin.site.register(City, AdminCity)
admin.site.register(Country)
admin.site.register(Profile)
admin.site.register(Category)
