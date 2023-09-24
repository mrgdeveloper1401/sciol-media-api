from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PostModel, PostOptionModel, TagPostModel
from .serializers import PostSerializers
from accounts.models import User

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = PostModel.objects.filter(is_active=True)
    permission_classes =''
    