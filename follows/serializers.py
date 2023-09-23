from rest_framework import serializers
from accounts.models import User


class RelationUser(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('',)