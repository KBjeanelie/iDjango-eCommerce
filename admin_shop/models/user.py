from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and save a User with the given email and password
        :param email:
        :param password:
        :return: User
        """

        if not email:
            raise ValueError("User must have an email ")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Create and save a staff user with the given email and password
        :param email:
        :param password:
        :return: user
        """

        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a super user with the given email and password
        :param email:
        :param password:
        :return: user
        """

        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=120)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a user admin not super user
    admin = models.BooleanField(default=False)  # a supper user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # email et password is required by default

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
