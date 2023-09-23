from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ChatModel, ChatOptionModel
from .serializers import ChatOptionSerializer, Chatserializers
from accounts.models import User


class ChatViewSet(viewsets.ViewSet):
    serializer_class = Chatserializers
    
    
    def list(self, request: Request):
        all_chat = ChatModel.objects.filter(is_active=True)
        all_chat_ser = self.serializer_class(all_chat)
        return Response(all_chat_ser.data, status=status.HTTP_200_OK)
        

    def create(self, request: Request):
        create_chat_ser = Chatserializers(data=request.data, many=True)
        if create_chat_ser.is_valid():
            create_chat_ser.save()
            return Response(create_chat_ser.data, status=status.HTTP_200_OK)
        return Response(create_chat_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request: Request, pk=None):
        chat = get_object_or_404(ChatModel, pk=pk)
        chat_ser = Chatserializers(chat)
        return Response(chat_ser.data, status=status.HTTP_200_OK)


    def update(self, request: Request, pk=None):
        update_chat = get_object_or_404(ChatModel, pk=pk)
        update_chat_ser = Chatserializers(update_chat, data=request.POST)
        if update_chat_ser.is_valid():
            update_chat_ser.save()
            return Response(update_chat_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_chat_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request: Request, pk=None):
        update_chat = get_object_or_404(ChatModel, pk=pk)
        update_chat_ser = Chatserializers(update_chat, data=request.POST, partial=True)
        if update_chat_ser.is_valid():
            update_chat_ser.save()
            return Response(update_chat_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_chat_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk=None):
        delete_chat = get_object_or_404(ChatModel, pk=pk)
        delete_chat.is_active = False
        delete_chat.save()
        return Response({'message': 'delete post successfly'})