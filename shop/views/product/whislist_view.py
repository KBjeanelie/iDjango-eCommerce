from django.views import View
from django.shortcuts import render, redirect

from admin_shop.models import WishList, user


class WishListView(View):
    template_name = 'shop/product/wishlist.html'

    def get(self, request):
        if request.user.is_authenticated:
            get_wishlist = WishList.objects.get(user=request.user)
            count_product = get_wishlist.products.all().count()
            if count_product >= 1:
                context_object = {'products': WishList.objects.products.all(), 'checked': True}
            else:
                context_object = {'checked': False}

            return render(request, self.template_name, context_object)

        else:
            return redirect(to='shop:login')
