from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .forms import RegisterForm, LoginForm, UpdateProfileForm
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserUpdateForm


def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


@login_required
def update_user(request):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, pk=request.user.id)
    if request.user != user:
        # Redirect if the logged-in user is not the same as the user to be edited
        return redirect(to='users:view-profile')

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            # Redirect to a success page
            return redirect(to='users:view-profile')
    else:
        form = UserUpdateForm(instance=user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit-profile.html', {'form': form,  'profile_form': profile_form})


class ViewUserProfileView(View):

    def get(self, request):
        return render(request, "user-profile.html")
