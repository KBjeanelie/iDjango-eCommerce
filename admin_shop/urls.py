from django.conf.urls.static import static
from django.urls import path

from admin_shop.views.account_view import AdminHomeView
from admin_shop.views.auth_view import AdminLoginView, AdminRegisterView
from admin_shop.views.product_view import AdminListProductView, AdminEditProductView, AdminProductDetailView, \
    AdminAddProductView
from eCommerce import settings

app_name = 'admin_shop'
urlpatterns = [

    # url pour le site
    path(
        route='dashboard/sign-in/',
        view=AdminLoginView.as_view(),
        name='login'
    ),
    path(
        route='dashboard/sign-up/',
        view=AdminRegisterView.as_view(),
        name='register'
    ),

    path(
        route='dashboard/home',
        view=AdminHomeView.as_view(),
        name='home'
    ),

    # URL FOR MANAGING PRODUCT
    path(
        route='dashboard/products/list-all-product/',
        view=AdminListProductView.as_view(),
        name='list-product'
    ),
    path(
        route='dashboard/products/edit-product/<str:slug>/',
        view=AdminEditProductView.as_view(),
        name='edit-product'
    ),
    path(
        route='dashboard/products/detail-of-product/<str:slug>/',
        view=AdminProductDetailView.as_view(),
        name='product-detail'
    ),
    path(
        route='dashboard/products/add',
        view=AdminAddProductView.as_view(),
        name='add-product'
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
