from rest_framework import serializers
from .models import PostModel, PostOptionModel, TagPostModel


class CreatePostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("user", 'body')

