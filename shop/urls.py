from django.urls import path

from shop.views.home_view import HomeView
from shop.views.product.shop_detail_view import ShopDetailView
from shop.views.product.shop_view import ShopView
from shop.views.product.whislist_view import WishListView
from shop.views.sites.about_view import AboutView
from shop.views.product.cart_view import CartView
from shop.views.product.checkout_view import CheckoutView
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
        name='services'
    ),

    # url for about product

    path(
        route='shop/cart',
        view=CartView.as_view(),
        name='cart'
    ),
    path(
        route='shop/products/product/whislist',
        view=WishListView.as_view(),
        name='wishlist'
    ),
    path(
        route='shop/products/checkout',
        view=CheckoutView.as_view(),
        name='checkout'
    ),

    # url for product
    path(
        route='shop/products/get-all',
        view=ShopView.as_view(),
        name='products'
    ),
    path(
        route='shop/products/shop-detail',
        view=ShopDetailView.as_view(),
        name='shop_detail'
    ),
]
