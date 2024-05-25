from django.urls import path
from . import views
from .views import RegisterView, CustomLoginView, UpdateUserView
from django.contrib.auth import views as auth_views


from .forms import LoginForm

app_name = "users"


urlpatterns = [
    path(
        "profile", views.ViewUserProfileView.as_view(), name="view-profile"
    ),

    path("profile/edit", UpdateUserView.as_view(), name="edit-profile"),


    path("register", RegisterView.as_view(), name="users-register"),

    path(
        "login",
        CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),

    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
