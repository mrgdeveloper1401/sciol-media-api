from rest_framework import serializers
from .models import User



class UserCreateAccountSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'first_name': {"required": True},
            'last_name': {'required': True},
            'email': {"required": True}
        }