from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'comment', views.CommentSerializers, basename='comment')


app_name = 'post'
urlpatterns = [
    path('comment/', include(router.urls))
] + router.urls