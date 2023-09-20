from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManagers


class User(AbstractUser):
    mobile = models.CharField(_('mobile phone'),
        max_length=11,
        unique=True,
        null=True
        )
    email_active_code = models.CharField(
        _('email active code'),
        max_length=128
    )
    

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user_model'
        

# class Active_code(models.Model):
#     email = models.EmailField(
#         _('email'),
#         unique=True,
        
#     )
#     code = models.PositiveIntegerField()
    
#     class Meta:
#         verbose_name = _('active code')
#         verbose_name_plural = _('active codes')
#         db_table = 'active-codes'
        