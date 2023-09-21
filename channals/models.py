from django.db import models
from core.models import CreateModel
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class ChannalModel(CreateModel):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator_channal')
    channal_name = models.CharField(_('channal name'), max_length=30)
    image_channal = models.ImageField(_('image channal'), upload_to='channal/image_channal/', null=True, blank=True)
    description = models.TextField(_('bio channal'), max_length=500)
    id_channal = models.SlugField(_('id'), max_length=50, null=True)
    members = models.ManyToManyField(User, related_name='members_channal')
    is_active = models.BooleanField(default=True)
    is_publish = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.creator} {self.channal_name}'
    
    class Meta:
        verbose_name = _('channal')
        verbose_name_plural = _('channals')
        db_table = 'channal-model'
        

class PostChannal(CreateModel):
    channal = models.ForeignKey(ChannalModel, on_delete=models.PROTECT, related_name='channal_option')
    content = models.TextField(_('type this here'), null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='channal/post_image/', blank=True)
    video = models.FileField(upload_to='channal/post_video', blank=True)
    file = models.FileField(upload_to='channal/post_file/', blank=True)
    
    class Meta:
        verbose_name = _('channal option')
        verbose_name_plural = _('channal options')
        db_table = 'channal-option-model'
        
class RecycleChannal(ChannalModel):
    class Meta:
        proxy = True
        
class RecycleChannalOption(PostChannal):
    class Meta:
        proxy = True