from django.conf import settings
from django.urls import path

from shop.views.home_view import HomeView
from shop.views.sites.about_view import AboutView
from shop.views.sites.contact_view import ContactView
from shop.views.sites.service_view import ServicesView

app_name = 'shop'
urlpatterns = [

    # url pour le site
    path(
        route='',
        view=HomeView.as_view(),
        name='home'
    ),
    path(
        route='shop/about-our-business',
        view=AboutView.as_view(),
        name='about'
    ),
    path(
        route='shop/contact-us',
        view=ContactView.as_view(),
        name='contact_us'
    ),
    path(
        route='shop/our_services-for-you',
        view=ServicesView.as_view(),
        name='our_services'
    )
]

