from rest_framework import serializers
from .models import GroupModel, GroupOptionModel


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'
    
    def create(self, validated_data):
        return GroupModel.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.members = validated_data.get('members', instance.members)
        instance.is_publish = validated_data.get('is_publish', instance.is_publish)
        return instance

class GroupOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupOptionModel
        fields = '__all__'