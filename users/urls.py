from django.urls import path
from . import views
from .views import home, profile, RegisterView

app_name = 'users'



urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('profile-management', views.ViewUserProfileView.as_view(), name='view-profile'),
    path('edit-management', views.ViewEditProfileView.as_view(), name='edit-profile'),
]

