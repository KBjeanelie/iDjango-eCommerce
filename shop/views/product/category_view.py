from django.views import View
from django.shortcuts import render
from django.views.generic import ListView

from admin_shop.models import Product


class CategoryListProductView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('prices')
    template_name = 'shop/product/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

