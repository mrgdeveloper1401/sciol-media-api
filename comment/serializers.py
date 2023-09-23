from rest_framework import serializers
from .models import CommentModel, CommentsOptionModel


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
        
    def create(self, validated_data):
        return CommentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', isinstance.post)
        instance.is_reply = validated_data.get('is_reply', instance.is_reply)
        return instance
        

class CommentOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentsOptionModel
        fields = '__all__'