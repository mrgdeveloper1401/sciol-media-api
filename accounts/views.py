from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserCreateAccountSerializers, ProfileSerializers
from .models import User


class UserCreateAccountView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateAccountSerializers


class ProfileApiview(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializers
    # permission_classes = (IsAuthenticated, )

