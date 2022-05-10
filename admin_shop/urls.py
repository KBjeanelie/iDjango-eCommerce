from django.conf.urls.static import static
from django.urls import path

from admin_shop.views.dashbord import DashbordView
from eCommerce import settings

app_name = 'admin_shop'
urlpatterns = [

    # url pour le site
    path(
        route='dashbord',
        view=DashbordView.as_view(),
        name='dashbord'
    ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
