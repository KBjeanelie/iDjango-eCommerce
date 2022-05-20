from django.shortcuts import render
from django.views import View


class AdminHomeView(View):
    template_name = 'admin_shop/sites/index.html'

    def get(self, request):
        return render(request, self.template_name)