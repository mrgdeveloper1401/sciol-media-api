from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views


router = SimpleRouter()
router.register(r'chat', views.ChatViewSet, basename='chat')

app_name = 'chat'
urlpatterns = [
    path('v1/', include(router.urls))
] + router.urls