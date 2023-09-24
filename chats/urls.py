from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views


router = DefaultRouter()
router.register = ('', views.ChatViewSet)

app_name = 'chats'
urlpatterns = [
    path('', include(router.urls))
] + router.urls