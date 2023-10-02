from rest_framework import serializers
from .models import CommentModel, CommentsOptionModel



class CommentOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentsOptionModel
        fields = '__all__'

        
class CommentSerializers(serializers.ModelSerializer):
    comment_option = CommentOptionSerializers(many=True, read_only=True)
    class Meta:
        model = CommentModel
        fields = (
            'user',
            'post',
            'body',
            'reply',
            'is_reply',
            'comment_option',
        )
        
        
        