from rest_framework import routers
from django.urls import include, path
from . import views


router = routers.SimpleRouter()
router.register = (r'channal', views.ChannalViewSet)

urlpatterns = [
    path('channal/', include(router.urls))
] + router.urls