from rest_framework import serializers
from .models import ChatModel, ChatOptionModel


class Chatserializers(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = '__all__'
        
    def create(self, validated_data):
        return ChatModel.objects.create(**validated_data)
        
        
class ChatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionModel
        fields = '__all__'