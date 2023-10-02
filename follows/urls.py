from rest_framework.routers import SimpleRouter
from django.urls import path
from django.urls import include
from . import views


router = SimpleRouter
router.register(r'ufollow', views.RelationUserViewSet, basename='follow-unfollow')

urlpatterns = [
    path('v1/', include(router.urls)),
    
] + router.urls
