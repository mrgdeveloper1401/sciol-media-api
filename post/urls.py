from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'post', views.PostViewSet, basename='home_post')


app_name = 'post'
urlpatterns = [
    path('', include(router.urls))
] + router.urls