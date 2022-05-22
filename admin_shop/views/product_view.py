from django.shortcuts import render
from django.views import View

from admin_shop.forms.category_form import CategoryCreationForm
from admin_shop.forms.marque_form import MarqueCreationForm
from admin_shop.forms.product_forms import ProductCreationForm


class AdminListProductView(View):
    template_name = 'admin_shop/products/product-list.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminProductDetailView(View):
    template_name = 'admin_shop/products/product-detail.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminAddProductView(View):
    template_name = 'admin_shop/products/product-add.html'
    context_object = {
        'product_add_form': ProductCreationForm,
        'category_form': CategoryCreationForm,
        'marque_form': MarqueCreationForm
    }

    def get(self, request, *args, **kwargs):
        print(self.context_object)
        return render(request, self.template_name, self.context_object)


class AdminEditProductView(View):
    template_name = 'admin_shop/products/product-edit.html'

    def get(self, request):
        return render(request, self.template_name)
