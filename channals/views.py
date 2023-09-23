from rest_framework import viewsets
from rest_framework.views import View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status




class ChannalViewSet(viewsets.ViewSet):
    def list(self, request: Request):
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