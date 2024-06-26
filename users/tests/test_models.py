from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile


class TestProfileModel(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='pravin', email='irpravin@gmail.com', password='pg030399'
        )

    def test_profile_creation(self):
        # Check if a profile is created automatically when a user is created
        profile_count = Profile.objects.count()
        # Ensure one profile exists after user creation
        self.assertEqual(profile_count, 1)

        # Check if the created profile matches the user
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        # Default address should be empty
        self.assertEqual(profile.address, '')

        # Update profile address and check
        profile.address = 'Tamilnadu, Chennai.'
        profile.save()
        self.assertEqual(profile.address, 'Tamilnadu, Chennai.')

    def test_profile_str_method(self):
        # Test the __str__ method of the Profile model
        profile = Profile.objects.get(user=self.user)
        # Expecting the username as the string representation
        self.assertEqual(str(profile), 'pravin')
