from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from core.models import CreateModel


class GroupModel(CreateModel):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator_group')
    group_name = models.CharField(_('group name'), max_length=30)
    description = models.TextField(_('bio group'), max_length=500)
    members = models.ManyToManyField(User, related_name='members_groups')
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.creator} {self.group_name}'
    
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        db_table = 'groups-model'

        
