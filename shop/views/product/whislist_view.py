from django.views import View
from django.shortcuts import render


class WishListView(View):
    template_name = 'shop/product/wishlist.html'

    def get(self, request):
        return render(request, self.template_name)
