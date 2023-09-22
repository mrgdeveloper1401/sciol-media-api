from rest_framework import serializers
from .models import User



class UserCreateAccountSerializers(serializers.ModelSerializer):    
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'mobile', 'password')
        extra_kwargs = {
            'first_name': {"required": True},
            'last_name': {'required': True},
            'email': {"required": True},
            'mobile': {'required': True, }
        }
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def validate_username(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('username cant be admin')
        elif 'root' in value:
            raise serializers.ValidationError('username cant be root')
        return value
    
    def validate_email(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('email cant be admin')
        elif 'root' in value:
            raise serializers.ValidationError('email cant be root')
        return value


