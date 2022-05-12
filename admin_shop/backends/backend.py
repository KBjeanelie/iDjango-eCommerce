from django.contrib.auth.backends import BaseBackend

from admin_shop.models import User


class SettingsBackend(BaseBackend):

    def authenticate(self, request, email, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            """
                User does not exist, let's create it
            """
            user = User.objects.create_superuser(email, password=password)

        if user is None:
            raise ValueError("Email adress is incorect")

        pwd_valid = user.check_password(password)

        if pwd_valid:
            return user
        else:
            return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
