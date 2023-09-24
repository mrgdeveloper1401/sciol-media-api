from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('create_user/', views.UserCreateAccountView.as_view(), name='create_user'),
    path('profile/<pk>/', views.ProfileApiview.as_view(), name='profile'),    
]