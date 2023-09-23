from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from .serializers import CommentOptionSerializers, CommentSerializers
from .models import CommentModel, CommentsOptionModel


class Commentviewset(viewsets.ViewSet):
    serializer_class = CommentSerializers
    
    
    def list(self, request: Request):
        all_comment = CommentModel.objects.filter(is_active=True)
        all_comment_ser = self.serializer_class(all_comment)
        return Response(all_comment_ser.data, status=status)
    
    def create(self, request: Request):
        comment_ser = self.serializer_class(data=request.data)
        if comment_ser.is_valid():
            comment_ser.save()
            return Response(comment_ser.data, status=status.HTTP_201_CREATED)
        return Response(comment_ser.errors)

    def retrieve(self, request: Request, pk=None):
        show_comment = get_object_or_404(CommentModel, pk=pk)
        show_comment_ser = self.serializer_class(show_comment)
        return Response(show_comment_ser.data, status=status.HTTP_200_OK)

    def update(self, request: Request, pk=None):
        update_comment = get_object_or_404(CommentModel, pk=pk)
        update_comment_ser = self.serializer_class(update_comment, data=request.data)
        if update_comment_ser.is_valid():
            update_comment_ser.save()
            return Response(update_comment_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_comment_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request: Request, pk=None):
        update_comment = get_object_or_404(CommentModel, pk=pk)
        update_comment_ser = self.serializer_class(update_comment, data=request.data, partial=True)
        if update_comment_ser.is_valid():
            update_comment_ser.save()
            return Response(update_comment_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_comment_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk=None):
        delete_comment = get_object_or_404(CommentModel, pk=pk)
        delete_comment.is_active = False
        delete_comment.save()
        return Response({'message': 'delete comment successfly'})