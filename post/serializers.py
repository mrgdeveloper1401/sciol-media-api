from rest_framework import serializers
from .models import PostModel, PostOptionModel, TagPostModel


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('user', 'body', 'post_tag')