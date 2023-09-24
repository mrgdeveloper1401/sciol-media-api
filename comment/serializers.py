from rest_framework import serializers
from .models import CommentModel, CommentsOptionModel


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

class CommentOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentsOptionModel
        fields = '__all__'