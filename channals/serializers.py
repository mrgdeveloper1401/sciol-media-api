from rest_framework import serializers
from .models import ChannalModel, PostChannal


class ChannalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChannalModel
        fileds = '__all__'
        
        
class ChannalOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostChannal
        fileds = '__all__'