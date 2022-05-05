from django.views import View
from django.shortcuts import render


class ShopView(View):
    template_name = 'shop/product/shop.html'

    def get(self, request):
        return render(request, self.template_name)
