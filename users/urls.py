from django.urls import path
from . import views
from .views import home, RegisterView, CustomLoginView, update_user
from django.contrib.auth import views as auth_views


from .forms import LoginForm

app_name = "users"


urlpatterns = [
    path(
        "profile-management", views.ViewUserProfileView.as_view(), name="view-profile"
    ),

    path("edit-management", update_user, name="edit-profile"),


    path("register/", RegisterView.as_view(), name="users-register"),

    path(
        "login/",
        CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
