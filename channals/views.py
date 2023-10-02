from rest_framework import viewsets
from rest_framework import filters
from .serializers import ChannalSerializers, ChannalOptionSerializers
from .models import ChannalModel


class ChannalViewSet(viewsets.ModelViewSet):
    queryset = ChannalModel.objects.filter(is_active=True)
    serializer_class = ChannalSerializers
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id_channal', )
    