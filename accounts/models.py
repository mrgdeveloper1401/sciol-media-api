from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    mobile = models.CharField(_('mobile phone'),
        max_length=11,
        unique=True
        )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user_model'