from django.views.generic import DetailView

from admin_shop.models import Product, Category


class CategoryListProductView(DetailView):
    model = Category
    template_name = 'shop/product/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object).order_by('prices')
        return context
