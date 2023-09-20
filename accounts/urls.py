from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserSignupView.as_view(), name='signup'),
    path('login/', views.UserSigninView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<str:email_active_code>/', views.ActiveAccountView.as_view(), name='active')
    
]