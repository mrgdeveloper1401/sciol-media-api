from rest_framework import serializers
from accounts.models import User
from .models import ChannalModel


class ChannalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChannalModel
        fileds = '__all__'