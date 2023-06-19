from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=120, blank=True, null=True)
    api_secret = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

    def has_valid_api_secret(self, secret_key: str) -> bool:
        return check_password(secret_key, self.api_secret)
