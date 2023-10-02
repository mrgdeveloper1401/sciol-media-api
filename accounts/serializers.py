from rest_framework import serializers
from .models import User, ImageuserModel
from rest_framework import viewsets


class UserAccountSerializers(serializers.ModelSerializer):    
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
      
      

class ProfileOptionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ImageuserModel
        fields = ('image',)
          
class ProfileSerializers(serializers.ModelSerializer):
    image = ProfileOptionSerializers(many=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
            'date_joined': {'write_only': True},
            'email_active_code': {'write_only': True, 'required': False},
            'password': {'write_only': True, 'required': False},
            'username': {'required': False},
            'gender': {'required': False},
            }
