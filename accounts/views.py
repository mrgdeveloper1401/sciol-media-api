from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateAccountSerializers, ProfileSerializers
from .models import User

# create account
class UserCreateAccountView(APIView):
    serializer_class = UserCreateAccountSerializers
    
    def post(self, request):
        ser_data_user = self.serializer_class(data=request.data)
        if ser_data_user.is_valid():
            ser_data_user.save()
            return Response(data=ser_data_user.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data_user.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
# complate profile
class ShowProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.filter(pk=pk)
        ser_data_user = ProfileSerializers(user, many=True)
        return Response(ser_data_user.data, status=status.HTTP_200_OK)
    

class UpdateProfileView(APIView):
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        update_ser = ProfileSerializers(user, data=request.data, partial=True)
        if update_ser.is_valid():
            update_ser.save()
            return Response(data=update_ser.data, status=status.HTTP_200_OK)
        return Response(data=update_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class DeleteProfileView(APIView):
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({'messages': 'successfly delete account'})
        