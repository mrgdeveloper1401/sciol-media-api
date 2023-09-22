from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateAccountSerializers
from .models import User


class UserCreateAccountView(APIView):
    serializer_class = UserCreateAccountSerializers
    
    def post(self, request):
        ser_data_user = self.serializer_class(data=request.data)
        if ser_data_user.is_valid():
            ser_data_user.save()
            return Response(data=ser_data_user.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data_user.errors, status=status.HTTP_400_BAD_REQUEST)