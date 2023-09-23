from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import UserCreateAccountSerializers, ProfileSerializers, UpdateProfileSerializers
from .models import User


# create account
class UserCreateAccountView(APIView):
    serializer_class = UserCreateAccountSerializers
    permission_classes = (IsAuthenticated, )
    
    def post(self, request: Request):
        ser_data_user = self.serializer_class(data=request.data)
        if ser_data_user.is_valid():
            ser_data_user.save()
            return Response(data=ser_data_user.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data_user.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
# complate profile
class ShowProfileView(APIView):
    def get(self, request: Request, pk):
        user = get_object_or_404(User, pk=pk)
        ser_data_user = ProfileSerializers(user)
        return Response(ser_data_user.data, status=status.HTTP_200_OK)
    

class UpdateProfileView(APIView):
    # permission_classes = (IsAuthenticated, )
    def put(self, request: Request, pk):
        user = User.objects.get(pk=pk)
        update_ser = UpdateProfileSerializers(user, data=request.data, partial=True)
        if update_ser.is_valid():
            update_ser.save()
            return Response(data=update_ser.data, status=status.HTTP_200_OK)
        return Response(data=update_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class DeleteProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    def delete(self, request: Request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({'messages': 'successfly delete account'})
        
        
# class UserViewSet(viewsets.ViewSet):
#     def list(self, request: Request):
#         pass

#     def create(self, request: Request):
#         pass

#     def retrieve(self, request: Request, pk=None):
#         pass

#     def update(self, request: Request, pk=None):
#         pass

#     def partial_update(self, request: Request, pk=None):
#         pass

#     def destroy(self, request: Request, pk=None):
#         pass