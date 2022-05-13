from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from admin_shop.backends.backend import SettingsBackend
from admin_shop.models import Profile, Cart, WishList, Country, City
from shop.forms import LoginForm, RegisterForm


class LogoutView(View):
    template_name = 'shop/user_account/login.html'
    context_object = {'login_form': LoginForm}

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name, self.context_object)


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

    def post(self, request, *args, **kwargs):
        r_form = RegisterForm(request.POST)

        passwd = r_form['password2'].value()
        if passwd and r_form['password'].value() and r_form['password2'].value() != passwd:
            raise ValueError("Password does not match.........")

        user = r_form.save(commit=False)
        user.set_password(passwd)
        user.save()
        r_form.save_m2m()

        user_cart = Cart(user=user)
        user_cart.save()

        user_wishlist = WishList(user=user)
        user_wishlist.save()

        default_country = Country.objects.get(name_country='France')
        default_city = City.objects.get(name_city='Paris')
        user_profile = Profile(user=user, country=default_country, city=default_city)
        user_profile.save()

        login(request, user)

        if user.is_admin:
            return redirect(to='/admin/')

        return redirect(to='shop:cart')
