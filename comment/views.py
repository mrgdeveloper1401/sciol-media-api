from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import CommentOptionSerializers, CommentSerializers


class Commentviewset(viewsets.ViewSet):
    
    
    
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass