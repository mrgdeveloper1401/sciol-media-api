from rest_framework import serializers
from .models import User, ImageuserModel
from rest_framework import viewsets


class UserAccountSerializers(serializers.ModelSerializer):    
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
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'mobile',
                  'birthday',
                  'gender',
                  )
        extra_kwargs = {
            'birthday': {'required': True},
            'gender': {'required': True},
            
        }
