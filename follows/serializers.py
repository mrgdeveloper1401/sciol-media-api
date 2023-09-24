from rest_framework import serializers
from accounts.models import User
from .models import RelationUserModel


class RelationUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'