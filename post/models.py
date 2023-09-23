from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import CreateModel
from accounts.models import User
from django.urls import reverse
from django.utils.text import slugify


class PostModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    body = models.TextField(max_length=500)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    post_tag = models.ManyToManyField('TagPostModel', blank=True, related_name='Ptag')
    
    def __str__(self):
        return f'{self.user} -- {self.body}'
    
    
    def get_absolute_url(self):
        return reverse("post:post_details", args=(self.id, self.slug))

    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'post-model'
        
        # order in database and show web
        ordering = ('-create_at', 'body', )
        
        
class TagPostModel(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'tag post'
        verbose_name_plural = 'tag posts'
        db_table = 'tag-post-model'
        

class PostOptionModel(models.Model):
    post = models.OneToOneField(PostModel, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='post/image', null=True, blank=True)
    video = models.FileField(upload_to='post/video', null=True, blank=True)

    def __str__(self) -> str:
        return str(self.post)[:30]
    
    class Meta:
        verbose_name = _('PostOptionModel')
        verbose_name_plural = _('PostOptionModels')
        db_table = 'post-option-models'
        
        
class RecyclePost(PostModel):
    class Meta:
        proxy = True
        

class RecyclePostOption(PostOptionModel):
    class Meta:
        proxy = True