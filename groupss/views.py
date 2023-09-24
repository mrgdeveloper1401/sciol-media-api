from rest_framework import viewsets
from rest_framework.views import View
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import GroupSerializers, GroupOptionSerializers
from .models import GroupModel, GroupOptionModel



class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.filter(is_active=True)
    serializers_class = GroupSerializers
    permission_classes = ''