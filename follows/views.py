from rest_framework.response import responses
from rest_framework import status
from rest_framework import viewsets
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from .serializers import RelationUserSerializers
from .models import RelationUserModel


class RelationUserViewSet(viewsets.ViewSet):
    serializer_class = RelationUserSerializers
    
    def list(self, request: Request):
        all_relation = RelationUserModel.objects.all()
        all_relation_ser = self.serializer_class(all_relation)
        return responses(all_relation_ser.data, status=status.HTTP_200_OK)
    
    def create(self, request: Request):
        create_relation_ser = self.serializer_class(data=request.data)
        if create_relation_ser.is_valid():
            create_relation_ser.save()
            return responses(create_relation_ser.data, status=status.HTTP_201_CREATED)
        return responses(create_relation_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request: Request, pk):
        delete_relation_user = get_object_or_404(RelationUserModel, pk=pk)
        delete_relation_user.delete()
        delete_relation_user.save()
        return responses({'message': 'unfollow user'})