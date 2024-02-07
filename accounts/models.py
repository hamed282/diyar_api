from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    national_code = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=150)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'national_code']

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# class OtpCode(models.Model):
#     phone_number = models.CharField(max_length=20)
#     code = models.IntegerField()
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.phone_number
