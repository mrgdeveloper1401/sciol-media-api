from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserSignupView.as_view(), name='signup'),
    path('login/', views.UserSigninView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
    
]