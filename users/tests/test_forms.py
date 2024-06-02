from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, UserEditForm, ProfileEditForm
from users.models import Profile


class TestUserForms(TestCase):

    def test_register_form_valid(self):
        # Prepare valid form data
        form_data = {
            'first_name': 'pravin',
            'last_name': 'kannappan',
            'username': 'irpravin',
            'email': 'irpravin@gmail.com',
            'password1': 'pg030399',
            'password2': 'pg030399',
        }

        # Create form instance with valid data
        form = UserRegisterForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_user_update_form_valid(self):
        # Create a User instance
        user = User.objects.create_user(
            username='irpravin',
            email='irpravin@gmail.com',
            password='pg030399'
        )

        # Prepare valid form data for user update
        form_data = {
            'first_name': 'Pravin Updated',
            'last_name': 'kannappan Updated',
            'email': 'irpravin_updated@gmail.com',
        }

        # Create form instance with valid data
        form = UserEditForm(data=form_data, instance=user)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_update_profile_form_valid(self):
        # Create a User instance
        user = User.objects.create_user(
            username='irpravin',
            email='irpravin_updated@gmail.com',
            password='pg030399'
        )

        # Prepare valid form data for profile update
        form_data = {
            'avatar': 'user/desktop/pravin.jpg',
            'address': 'Tamilnadu, Chennai',
        }

        # Retrieve the user's profile or create one if it doesn't exist
        profile, created = Profile.objects.get_or_create(user=user)

        # Create form instance with valid data
        form = ProfileEditForm(data=form_data, instance=profile)

        # Check if the form is valid
        self.assertTrue(form.is_valid())
