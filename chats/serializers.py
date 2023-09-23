from rest_framework import serializers
from .models import ChatModel, ChatOptionModel


class Chatserializers(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = '__all__'
        
        
class ChatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionModel
        fields = '__all__'