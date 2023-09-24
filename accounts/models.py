from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel
from django.utils import timezone



class User(AbstractUser):
    mobile = models.CharField(_('mobile phone'),
        max_length=11,
        unique=True,
        null=True
        )
    birthday = models.DateField(_("Birth day"), default=timezone.now)
    genders = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = models.CharField(_("Gender"), max_length=6, choices=genders)

    email_active_code = models.CharField(
        _('email active code'),
        max_length=128
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user_model'
        
class ImageuserModel(CreateModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='profile')
    
    class Meta:
        verbose_name = _('image user')
        verbose_name_plural = _('image users')
        db_table = 'image_user_model'
        
class RecycleUser(User):
    class Meta:
        proxy = True

