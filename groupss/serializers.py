from rest_framework import serializers
from .models import GroupModel, GroupOptionModel


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'