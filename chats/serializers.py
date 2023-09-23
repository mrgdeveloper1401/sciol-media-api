from rest_framework import serializers
from .models import ChatModel, ChatOptionModel


class Chatserializers(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = '__all__'
        
    def create(self, validated_data):
        return ChatModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        return instance
        
        
class ChatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionModel
        fields = '__all__'