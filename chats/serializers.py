from rest_framework import serializers
from .models import ChatModel, ChatOptionModel


class Chatserializers(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = (
            'from_user',
            'to_user',
            'body',
            'create_at',
        )

        
class ChatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionModel
        fields = '__all__'