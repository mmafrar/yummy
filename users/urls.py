from django.urls import path
from . import views
from .views import home, profile, RegisterView, CustomLoginView
from django.contrib.auth import views as auth_views

# added by naqibullah
from .forms import LoginForm

app_name = "users"


urlpatterns = [
    path("", home, name="users-home"),
    path('profile/', profile, name='users-profile'),
    path(
        "profile-management", views.ViewUserProfileView.as_view(), name="view-profile"
    ),

    path("edit-management", views.ViewEditProfileView.as_view(), name="edit-profile"),


    ###################### Cleaned Code ####################################################

    path("register/", RegisterView.as_view(), name="users-register"),
    # brought from Main URL to here by naqibullah
    path(
        "login/",
        CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
    # updated the code
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
