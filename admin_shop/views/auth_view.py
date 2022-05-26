from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from admin_shop.forms.auth_forms import AdminLoginForm, AdminRegisterForm


class AdminLoginView(View):
    template_name = 'admin_shop/auth/login.html'
    context_object = {'admin_login_form': AdminLoginForm}

    def get(self, request):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        admin_form = AdminLoginForm(request.POST)
        email = admin_form['email'].value()
        password = admin_form['password'].value()
        user = authenticate(request, email=email, password=password)

        if user is None:
            redirect(to='dashboard:login')

        if user.is_admin:
            redirect(to='dashboard:home')
        else:
            redirect(to='dashboard:login')


class AdminRegisterView(View):
    template_name = 'admin_shop/auth/register.html'
    context_object = {'admin_register_form': AdminRegisterForm}

    def get(self, request):
        return render(request, self.template_name, self.context_object)


class AdminLockView(View):
    template_name = 'admin_shop/auth/lock.html'

    def get(self, request):
        return render(request, self.template_name)
