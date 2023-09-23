from rest_framework import routers
from django.urls import path
from django.urls import include
from . import views


router = routers.SimpleRouter()
router.register(r'ufollow', views.RelationUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
] + router.urls
