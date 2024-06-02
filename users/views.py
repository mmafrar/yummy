import os
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile
from .forms import UserRegisterForm, UserLoginForm, UserEditForm, ProfileEditForm


class UserRegisterView(View):
    form_class = UserRegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to=settings.LOGIN_REDIRECT_URL)

        # else process dispatch as it otherwise normally would
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('users:login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class UserLoginView(LoginView):
    form_class = UserLoginForm

    def get_success_url(self):
        redirect_to = self.request.GET.get('redirect_to')
        # redirect based on the user type
        if self.request.user.is_superuser:
            return settings.DASHBOARD_REDIRECT_URL
        elif redirect_to:
            return redirect_to
        return settings.LOGIN_REDIRECT_URL


class ProfileDetailView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "profile-detail.html")


class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'profile-edit.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.id)
        form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.id)
        if request.user != user:
            # Redirect if the logged-in user is not the same as the user to be edited
            return redirect(to='users:profile.show')

        form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            image_path = profile.avatar.path

            if profile.avatar != 'users/default.jpg':
                if 'avatar' in request.FILES:
                    if os.path.exists(image_path):
                        os.remove(image_path)
            form.save()
            profile_form.save()

            # Redirect to a success page
            messages.success(request, 'Profile has been updated succesfully')
            return redirect(to='users:profile.show')

        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})
