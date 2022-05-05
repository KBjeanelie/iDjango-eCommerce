from django.views import View
from django.shortcuts import render


class ShopDetailView(View):
    template_name = 'shop/product/shop-detail.html'

    def get(self, request):
        return render(request, self.template_name)
