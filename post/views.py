from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import PostModel, PostOptionModel, TagPostModel
from .serializers import PostSerializers

class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializers
    queryset = PostModel.objects.all()
    
    def list(self, request):
        post_ser = self.serializer_class(self.queryset, many=True)
        return Response(post_ser.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        pass
    
    def retrieve(self, request, pk=None):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass