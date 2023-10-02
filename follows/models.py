from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel
from accounts.models import User



class RelationUserModel(CreateModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    class Meta:
        verbose_name = _('relation')
        verbose_name_plural = _('relations')
        db_table = 'relation-model'
        
    def __str__(self) -> str:
        return f'{self.from_user}  {self.to_user}'
    
    
class RecycleRelationUser(RelationUserModel):
    class Meta:
        proxy = True