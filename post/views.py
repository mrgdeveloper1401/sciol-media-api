from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework import filters
from .models import PostModel, PostOptionModel, TagPostModel
from .serializers import PostSerializers

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = PostModel.objects.filter(is_active=True)
    permission_classes =''
    filter_backends = (filters.SearchFilter,)
    search_fields = ('body', )
    