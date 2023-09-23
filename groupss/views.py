from rest_framework import viewsets
from rest_framework.views import View
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import GroupSerializers, GroupOptionSerializers
from .models import GroupModel, GroupOptionModel



class GroupViewSet(viewsets.ViewSet):
    serializers_class = GroupSerializers


    
    def list(self, request):
        all_group = GroupSerializers.objects.filter(is_active=True, is_publish=True)
        all_group_ser = self.serializer_class(all_group)
        return Response(all_group_ser.data, status=status)
    
    def create(self, request):
        group_ser = self.serializer_class(data=request.data)
        if group_ser.is_valid():
            group_ser.save()
            return Response(group_ser.data, status=status.HTTP_201_CREATED)
        return Response(group_ser.errors)

    def retrieve(self, request, pk=None):
        show_group = get_object_or_404(GroupModel, pk=pk)
        show_group_ser = self.serializer_class(show_group)
        return Response(show_group_ser.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        update_group = get_object_or_404(GroupModel, pk=pk)
        update_group_ser = self.serializer_class(update_group, data=request.data)
        if update_group_ser.is_valid():
            update_group_ser.save()
            return Response(update_group_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_group_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        update_group = get_object_or_404(GroupModel, pk=pk)
        update_group_ser = self.serializer_class(update_group, data=request.data, partial=True)
        if update_group_ser.is_valid():
            update_group_ser.save()
            return Response(update_group_ser.data, status=status.HTTP_201_CREATED)
        return Response(update_group_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        delete_group = get_object_or_404(GroupModel, pk=pk)
        delete_group.is_active = False
        delete_group.save()
        return Response({'message': 'delete comment successfly'})