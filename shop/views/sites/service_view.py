from django.views import View
from django.shortcuts import render


class ServicesView(View):
    template_name = 'shop/sites/service.html'

    def get(self, request):
        return render(request, self.template_name)