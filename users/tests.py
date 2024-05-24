from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# Unit Testing

# The purpose of these unit tests is to ensure that the individual units of Users application
# are functioning correctly in isolation.


class UserAndProfileTestCase(TestCase):
    def setUp(self):
        # Create a user object
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'testpassword')
        # Create a profile object linked to the user
        self.profile = Profile.objects.create(
            user=self.user, address='123 Test St', avatar='users/default.jpg')

    def test_user_creation(self):
        """Test the user creation process"""
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_user_profile(self):
        """Test the user's linked profile"""
        user = User.objects.get(username='testuser')
        self.assertEqual(user.profile.address, '123 Test St')

    def test_profile_creation(self):
        """Test the profile creation process"""
        self.assertEqual(self.profile.address, '123 Test St')
        self.assertEqual(self.profile.avatar, 'users/default.jpg')

    def test_profile_link_to_user(self):
        """Test the one-to-one link between User and Profile"""
        self.assertEqual(self.profile.user, self.user)
