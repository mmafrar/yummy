from django.urls import path
from django.contrib.auth.views import LogoutView as UserLogoutView

from .forms import UserLoginForm
from .views import UserRegisterView, UserLoginView, ProfileDetailView, ProfileEditView


app_name = "users"


urlpatterns = [
    path("register", UserRegisterView.as_view(), name="register"),
    path("login", UserLoginView.as_view(redirect_authenticated_user=True,
         template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path("logout", UserLogoutView.as_view(), name="logout"),
    path("profile", ProfileDetailView.as_view(), name="profile.show"),
    path("profile/edit", ProfileEditView.as_view(), name="profile.edit"),
]
