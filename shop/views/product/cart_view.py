from django.views import View
from django.shortcuts import render, redirect

from admin_shop.models import Cart


class CartView(View):
    template_name = 'shop/product/cart.html'

    def get(self, request):
        if request.user.is_authenticated:
            get_wishlist = Cart.objects.get(user=request.user)
            count_product = get_wishlist.products.all().count()
            if count_product >= 1:
                context_object = {'products': Cart.objects.products.all(), 'checked': True}
            else:
                count_product = 0
                context_object = {'checked': False, 'count': count_product}

            return render(request, self.template_name, context_object)
        else:
            return redirect(to='shop:login')
