from django.test import TestCase
from django.urls import reverse

# Testcase to verify the url for each path of the application
class TestUrls(TestCase):
    # URL Profile
    def test_view_profile_url(self):
        url = reverse('users:view-profile')
        self.assertEqual(url, '/users/profile')
    # URL Profile edit
    def test_edit_profile_url(self):
        url = reverse('users:edit-profile')
        self.assertEqual(url, '/users/profile/edit')
    # URL user register
    def test_register_url(self):
        url = reverse('users:users-register')
        self.assertEqual(url, '/users/register')
    # URL Users login
    def test_login_url(self):
        url = reverse('users:login')
        self.assertEqual(url, '/users/login')
    # URL user logout
    def test_logout_url(self):
        url = reverse('users:logout')
        self.assertEqual(url, '/users/logout')
