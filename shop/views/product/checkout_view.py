from django.views import View
from django.shortcuts import render


class CheckoutView(View):
    template_name = 'shop/product/checkout.html'

    def get(self, request):
        return render(request, self.template_name)