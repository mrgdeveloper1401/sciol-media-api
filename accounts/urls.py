from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('create/', views.UserCreateAccountView.as_view(),name='create_user'),
    path('show-profile/<int:pk>/', views.ShowProfileView.as_view(), name='show_profile'),
    path('update-profile/<int:pk>/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('delete-profile/<int:pk>/', views.DeleteProfileView.as_view(), name='delete_profile'),
    
]