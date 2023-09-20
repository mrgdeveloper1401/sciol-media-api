from django.db import models
from core.models import CreateModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from accounts.models import User
from post.models import PostModel


class CommentModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='pcomment')
    body = models.TextField(max_length=400)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomment', blank=True, null=True)
    is_reply = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        db_table = 'comment-model'
        ordering = ('-create_at', 'body', )
        
    def __str__(self) -> str:
        return f'{self.user} - {self.body[:30]}'
    
    
class CommentsOptionModel(models.Model):
    comment = models.OneToOneField(PostModel, on_delete=models.PROTECT)
    image = models.FileField(upload_to='post/image', null=True, blank=True)
    video = models.FileField(upload_to='post/video', null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.comment)[:30]
    
    class Meta:
        verbose_name = 'CommentOption'
        verbose_name_plural = 'CommentOptions'
        db_table = 'comment-option-model'
        
    
class RecycleComment(CommentModel):
    class Meta:
        proxy = True