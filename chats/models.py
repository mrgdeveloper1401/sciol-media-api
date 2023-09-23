from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel
from accounts.models import User



class ChatModel(CreateModel):
    from_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='frchat')
    to_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tochat')
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.from_user}  {self.to_user}'
    
    class Meta:
        verbose_name = _('chat')
        verbose_name_plural = _('chats')
        db_table = 'chat-model'
        

class RecycleChat(ChatModel):
    class Meta:
        proxy = True

class ChatOptionModel(CreateModel):
    chat = models.ForeignKey(ChatModel, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='chat/image', null=True, blank=True)
    video = models.FileField(upload_to='chat/video', null=True, blank=True)
    file = models.FileField(upload_to='chat/file', null=True, blank=True)
    
    # def __str__(self):
    #     return self.option
        
    class Meta:
        verbose_name = _('chat option')
        verbose_name_plural = _('chat options')
        db_table = 'chat-option-model'
        

class RecycleChatOption(ChatOptionModel):
    class Meta:
        proxy = True