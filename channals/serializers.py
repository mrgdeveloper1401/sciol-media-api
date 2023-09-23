from rest_framework import serializers
from accounts.models import User
from .models import ChannalModel, PostChannal


class ChannalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChannalModel
        exclude = ('creator', )
        
        
    def create(self, validated_data):
        return ChannalModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.channal_name = validated_data.get('channal_name', isinstance.channal_name)
        instance.image_channal = validated_data.get('image_channal', isinstance.image_channal)
        instance.description = validated_data.get('description', isinstance.description)
        instance.id_channal = validated_data.get('id_channal', isinstance.id_channal)
        instance.members = validated_data.get('members', isinstance.members)
        instance.is_publish = validated_data.get('is_publish', isinstance.is_publish)
        return instance