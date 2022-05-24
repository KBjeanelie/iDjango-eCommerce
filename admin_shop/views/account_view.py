from django.shortcuts import render, redirect
from django.views import View

from admin_shop.forms.user_auth import ProfileForm


class AdminHomeView(View):
    template_name = 'admin_shop/sites/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect(to='dashboard:login')


class AdminProfileView(View):
    template_name = 'admin_shop/profile/profile.html'
    context_object = {'profile_form': ProfileForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)
