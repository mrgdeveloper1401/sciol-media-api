from rest_framework import serializers
from .models import PostModel, PostOptionModel, TagPostModel


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'

    def create(self, validated_data):
        return PostModel.objects.create(**validated_data)