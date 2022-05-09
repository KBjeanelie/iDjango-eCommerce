from django.urls import path

from user_account.views.login_view import LoginView

app_name = "user_account"

urlpatterns = [

    # url pour le site
    path(
        route='sign-in',
        view=LoginView.as_view(),
        name='login'
    ),
]