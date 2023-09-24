from rest_framework import serializers
from .models import PostModel, PostOptionModel, TagPostModel


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        
        
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = TagPostModel
        fields = '__all__'
        
        
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostOptionModel
        fields = '__all__'