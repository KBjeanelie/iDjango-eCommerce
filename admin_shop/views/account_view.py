from django.shortcuts import render
from django.views import View

from admin_shop.forms.user_auth import ProfileForm


class AdminHomeView(View):
    template_name = 'admin_shop/sites/index.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminProfileView(View):
    template_name = 'admin_shop/profile/profile.html'
    context_object = {'profile_form': ProfileForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)
