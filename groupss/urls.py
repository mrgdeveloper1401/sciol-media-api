from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.SimpleRouter()
router.register = (r'grup', views.GroupViewSet)

urlpatterns = [
    path('group', include(router.urls))
] + router.urls