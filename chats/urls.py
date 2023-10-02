from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views


router = DefaultRouter()
router.register = ('', views.ChatViewSet)

urlpatterns = [
    path('', include(router.urls))
] + router.urls