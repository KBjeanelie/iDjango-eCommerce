from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from admin_shop.backends.backend import SettingsBackend
from shop.forms import LoginForm, RegisterForm


class LoginView(View):
    template_name = 'shop/user_account/login.html'
    context_object = {'login_form': LoginForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        sign_form = LoginForm(request.POST)
        email = sign_form['email'].value()
        password = sign_form['password'].value()
        user = authenticate(request, email=email, password=password)

        if user is None:
            return redirect(to='shop:login')
        login(request, user)

        if user.is_admin:
            return redirect(to='/admin/')
        return redirect(to='shop:cart')


class RegisterView(View):
    template_name = 'shop/user_account/register.html'

    context_object = {'register_form': RegisterForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)
