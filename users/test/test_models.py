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
        # Check if a profile is created when a user is created
        profile_count_before = Profile.objects.count()
        self.assertEqual(profile_count_before, 0)  # Ensure no profiles exist yet

        # Create a profile for the user
        profile = Profile.objects.create(user=self.user, address='Tamilnadu, Chennai.')

        # Check if the profile was created successfully
        profile_count_after = Profile.objects.count()
        self.assertEqual(profile_count_after, 1)  # Expecting one profile after creation

        # Check if the created profile matches the user
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.address, 'Tamilnadu, Chennai.')

    def test_profile_str_method(self):
        # Test the __str__ method of the Profile model
        profile = Profile.objects.create(user=self.user, address='Tamilnadu, Chennai')
        self.assertEqual(str(profile), 'pravin')  # Expecting the username as the string representation
