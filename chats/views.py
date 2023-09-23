from rest_framework import viewsets
from .models import ChatModel, ChatOptionModel
from .serializers import ChatOptionSerializer, Chatserializers


class ChatViewSet(viewsets.ViewSet):
    serializer_class = Chatserializers
    
    
    def list(self, request):
        all_chat = ChatModel.objects.filter(is_active=True)
        
        

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass