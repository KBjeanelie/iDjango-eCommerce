from django.urls import path

from user_account.views.login_view import LoginView

app_name = "user_account"

urlpatterns = [

    # url pour le site
    path(
        route='login',
        view=LoginView.as_view(),
        name='login'
    ),
]