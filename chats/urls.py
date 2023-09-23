from rest_framework import routers
from django.urls import include, path
from . import views


router = routers.SimpleRouter()
router.register = (r'chat', views.ChatViewSet)

urlpatterns = [
    path('chat/', include(router.urls))
] + router.urls