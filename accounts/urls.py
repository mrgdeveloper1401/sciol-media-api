from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', views.UserViewset, basename='user')

app_name = 'accounts'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('profile/<int:pk>/', views.ProfileApiView.as_view(), name='profile')
] + router.urls