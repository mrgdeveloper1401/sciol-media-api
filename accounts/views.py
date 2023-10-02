from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import UserAccountSerializers, ProfileSerializers, ProfileOptionSerializers
from .models import User, ImageuserModel


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializers


class ProfileApiview(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializers
    # permission_classes = (IsAuthenticated, )


class profileOptionApiView(RetrieveUpdateAPIView):
    queryset = ImageuserModel.objects.all()
    serializer_class = ProfileOptionSerializers