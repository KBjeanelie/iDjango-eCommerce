from django.shortcuts import render, redirect
from django.views import View


class AdminLoginView(View):
    template_name = 'admin_shop/auth/login.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminRegisterView(View):
    template_name = 'admin_shop/auth/register.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminLockView(View):
    template_name = 'admin_shop/auth/lock.html'

    def get(self, request):
        return render(request, self.template_name)
