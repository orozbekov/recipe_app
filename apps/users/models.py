from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField("Электронный адрес", unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']

    def __str__(self):
        return self.username

    objects = CustomUserManager()
