from rest_framework import viewsets
from .models import ChatModel
from .serializers import Chatserializers
from rest_framework import filters


class ChatViewSet(viewsets.ModelViewSet):
    queryset = ChatModel.objects.filter(is_active=True)
    serializer_class = Chatserializers
    permission_classes = ''
    filter_backends = (filters.SearchFilter, )
    search_fileds = ('body', )