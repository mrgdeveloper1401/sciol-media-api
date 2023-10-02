from rest_framework import serializers
from .models import CommentModel, CommentsOptionModel
from accounts.views import UserRetiveApiView


class CommentOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentsOptionModel
        fields = '__all__'

        
class CommentSerializers(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name='accounts:show_profile')
    class Meta:
        model = CommentModel
        fields = (
            'user',
            'post',
            'body',
            'reply',
            'is_reply',
            'user'
        )
        
        
        