from rest_framework import viewsets
from .serializers import CommentOptionSerializers, CommentSerializers
from .models import CommentModel, CommentsOptionModel


class Commentviewset(viewsets.ModelViewSet):
    queryset = CommentModel.objects.filter(is_active=True)
    serializer_class = CommentSerializers
    

