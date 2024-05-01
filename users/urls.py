from django.urls import path
from . import views

app_name = 'users'



urlpatterns = [
    path('profile-management', views.ViewUserProfileView.as_view(), name='view-profile'),
    path('edit-management', views.ViewEditProfileView.as_view(), name='edit-profile'),
]
