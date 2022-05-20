from django.conf.urls.static import static
from django.urls import path

from admin_shop.views.account_view import AdminHomeView
from admin_shop.views.auth_view import AdminLoginView, AdminRegisterView
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

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
