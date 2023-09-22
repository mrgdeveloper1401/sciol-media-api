from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('api-user/', views.UserCreateAccountView.as_view(),name='create_user'),
    
]