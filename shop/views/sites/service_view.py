from django.views import View
from django.shortcuts import render


class ServicesView(View):
    template_name = ''

    def get(self, request):
        return render(request, self.template_name)