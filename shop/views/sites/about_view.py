from django.views import View
from django.shortcuts import render


class AboutView(View):
    template_name = 'shop/sites/about.html'

    def get(self, request):
        return render(request, self.template_name)