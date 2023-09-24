from rest_framework import viewsets
from rest_framework.views import View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from .serializers import ChannalSerializers, ChannalOptionSerializers
from .models import ChannalModel





# class ChannalViewSet(viewsets.ViewSet):
#     serialzer_class = ChannalSerializers
    
#     def list(self, request: Request):
#         all_channal = get_object_or_404(ChannalModel)
#         channal_ser = self.serialzer_class(all_channal)
#         return Response(channal_ser.data, status=status.HTTP_200_OK)

#     def create(self, request: Request):
#         channal_ser = ChannalSerializers(data=request.data, many=True)
#         if channal_ser.is_valid():
#             channal_ser.save()
#             return Response(channal_ser.data, status=status.HTTP_201_CREATED)
#         return Response(channal_ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request: Request, pk=None):
#         my_channal = get_object_or_404(ChannalModel, pk=pk)
#         my_channal_ser = ChannalSerializers(my_channal)
#         return Response(my_channal_ser.data, status=status.HTTP_200_OK)

#     def update(self, request: Request, pk=None):
#         update_channal = get_object_or_404(ChannalModel, pk=pk)
#         update_channal_ser = ChannalSerializers(update_channal, data=request.data)
#         if update_channal_ser.is_valid():
#             update_channal_ser.save()
#             return Response(update_channal_ser.data, status=status.HTTP_201_CREATED)
#         return Response(update_channal_ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         update_channal = get_object_or_404(ChannalModel, pk=pk)
#         update_channal_ser = ChannalSerializers(update_channal, data=request.data, partial=True)
#         if update_channal_ser.is_valid():
#             update_channal_ser.save()
#             return Response(update_channal_ser.data, status=status.HTTP_201_CREATED)
#         return Response(update_channal_ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         delete_channal = get_object_or_404(ChannalModel, pk=pk)
#         delete_channal.is_active = False
#         delete_channal.save()
#         return Response({'message': 'delete channal success'})
    

class ChannalViewSet(viewsets.ModelViewSet):
    queryset = ChannalModel.objects.filter(is_active=True)
    serializer_class = ChannalSerializers