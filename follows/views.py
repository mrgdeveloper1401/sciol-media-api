from rest_framework import viewsets
from .serializers import RelationUserSerializers
from .models import RelationUserModel


class RelationUserViewSet(viewsets.ModelViewSet):
    queryset = RelationUserModel.objects.all()
    serializer_class = RelationUserSerializers
    permission_classes = ''
    filterset_fields = ('body', )