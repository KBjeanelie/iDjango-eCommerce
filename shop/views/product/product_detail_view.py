from django.views.generic import DetailView
from admin_shop.models import Product


class ProductDetailView(DetailView):

    model = Product

    template_name = 'shop/product/shop-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        context['lastestProducts'] = Product.objects.all().order_by('-date_add')
        return context

