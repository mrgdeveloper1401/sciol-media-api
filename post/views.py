from rest_framework import viewsets
from .serializers import CreatePostSerializers
from .models import PostModel, PostOptionModel, TagPostModel


class PostView(viewsets.ViewSet):
    def list(self, request):
        ...