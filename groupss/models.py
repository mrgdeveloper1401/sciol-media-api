from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from core.models import CreateModel


class GroupModel(CreateModel):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator_group')
    group_name = models.CharField(_('group name'), max_length=30)
    image = models.ImageField(_('image group'), upload_to='group/image_group', null=True, blank=True)
    id_group = models.SlugField(_('id group'), null=True)
    description = models.TextField(_('bio group'), max_length=500)
    members = models.ManyToManyField(User, related_name='members_groups')
    is_active = models.BooleanField(default=True)
    is_publish = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.creator} {self.group_name}'
    
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        db_table = 'groups-model'
        

class GroupOptionModel(CreateModel):
    grup = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='group_option')
    body = models.TextField()
    image = models.ImageField(upload_to='gruop/image_group', blank=True)
    video = models.FileField(upload_to='group/group_video', blank=True)
    file = models.FileField(upload_to='group/group_file', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('group option')
        verbose_name_plural = _('group options')
        db_table = 'groups-option-model'