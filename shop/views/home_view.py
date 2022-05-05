from django.views.generic import ListView
from admin_shop.models.product import Product


class HomeView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-date_add')[:10]
    template_name = 'shop/sites/index.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        return context
