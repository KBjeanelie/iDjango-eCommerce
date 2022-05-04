from django.views import View
from django.shortcuts import render


class CartView(View):
    template_name = 'shop/product/cart.html'

    def get(self, request):
        return render(request, self.template_name)
