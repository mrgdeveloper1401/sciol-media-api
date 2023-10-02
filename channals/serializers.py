from rest_framework import serializers
from .models import ChannalModel, PostChannal


class ChannalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChannalModel
        exclude = ('is_active', )
        
        
class ChannalOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostChannal
        fields = '__all__'