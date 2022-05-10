from django.conf.urls.static import static
from django.urls import path

from eCommerce import settings
from shop.views.home_view import HomeView
from shop.views.product.product_detail_view import ProductDetailView
from shop.views.product.category_view import CategoryListProductView
from shop.views.product.whislist_view import WishListView
from shop.views.sites.about_view import AboutView
from shop.views.product.cart_view import CartView
from shop.views.product.checkout_view import CheckoutView
from shop.views.sites.contact_view import ContactView
from shop.views.sites.service_view import ServicesView
from shop.views.user_account.auth_view import LoginView, RegisterView

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
        route='shop/fashion-modes/categories/<str:slug>/',
        view=CategoryListProductView.as_view(),
        name='category_view'
    ),
    path(
        route='shop/fashion-modes/categories/<str:cat_slug>/<str:slug>/',
        view=ProductDetailView.as_view(),
        name='product_detail'
    ),

    # url for authentification
    path(
        route='shop/user-account/sign-in/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='shop/user-account/sign-up/',
        view=RegisterView.as_view(),
        name='register'
    )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
