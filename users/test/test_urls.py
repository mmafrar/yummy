from django.test import TestCase
from django.urls import reverse

class TestUrls(TestCase):
    def test_view_profile_url(self):
        url = reverse('users:view-profile')
        self.assertEqual(url, '/users/profile-management')

    def test_edit_profile_url(self):
        url = reverse('users:edit-profile')
        self.assertEqual(url, '/users/edit-management')

    def test_register_url(self):
        url = reverse('users:users-register')
        self.assertEqual(url, '/users/register/')

    def test_login_url(self):
        url = reverse('users:login')
        self.assertEqual(url, '/users/login/')

    def test_logout_url(self):
        url = reverse('users:logout')
        self.assertEqual(url, '/users/logout/')
