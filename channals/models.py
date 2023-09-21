from django.db import models
from core.models import CreateModel
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class ChannalModel(CreateModel):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator_channal')
    channal_name = models.CharField(_('channal name'), max_length=30)
    description = models.TextField(_('bio channal'), max_length=500)
    members = models.ManyToManyField(User, related_name='members_channal')
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    is_publish = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.creator} {self.channal_name}'
    
    class Meta:
        verbose_name = _('channal')
        verbose_name_plural = _('channals')
        db_table = 'channal-model'
        