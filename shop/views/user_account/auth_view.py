from django.shortcuts import render
from django.views import View


class LoginView(View):
    template_name = 'shop/user_account/login.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'shop/user_account/register.html'

    def get(self, request):
        return render(request, self.template_name)
