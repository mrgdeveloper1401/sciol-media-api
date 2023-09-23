from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PostModel, PostOptionModel, TagPostModel
from .serializers import PostSerializers
from accounts.models import User

class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializers
    queryset = PostModel.objects.all()
    
    def list(self, request):
        post_ser = self.serializer_class(self.queryset, many=True)
        return Response(post_ser.data, status=status.HTTP_200_OK)
    
    def create(self, request, pk=None):
        user = User.objects.get(pk=pk)
        post_ser = self.serializer_class(user, data=request.data, many=True)
        if post_ser.is_valid():
            post_ser.save()
            return Response(data=post_ser.data, status=status.HTTP_201_CREATED)
        return Response(post_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        show_post = get_object_or_404(self.queryset, pk=pk)
        post_ser = self.serializer_class(show_post, many=True)
        return Response(data=post_ser.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        post_ser = self.serializer_class(post, data=request.data, partial=True)
        if post_ser.is_valid():
            post_ser.save()
            return Response(data=post_ser.data, status=status.HTTP_201_CREATED)
        return Response(post_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        post.is_active = False
        post.save()
        return Response({'message': 'succesfly delete post'})