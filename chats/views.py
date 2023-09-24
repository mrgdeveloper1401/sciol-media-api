from rest_framework import viewsets
from .models import ChatModel, ChatOptionModel
from .serializers import ChatOptionSerializer, Chatserializers


class ChatViewSet(viewsets.ModelViewSet):
    queryset = ChatModel.objects.filter(is_active=True)
    serializer_class = Chatserializers
    permission_classes = ''