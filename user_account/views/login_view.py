from django.shortcuts import render
from django.views import View


class LoginView(View):
    template_name = "user_account/base.html"

    def get(self, request):
        return render(request, self.template_name)