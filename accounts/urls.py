from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='signup'),
    path('login/', views.UserSigninView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
    
]