from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from users.views import RegisterView, CustomLoginView, UpdateUserView, ViewUserProfileView


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='mash', email='mash@gmail.com', password='Tinksg0303!kk')
        self.user.save()

    def test_register_view_get(self):
        # Test GET request to register view
        request = self.factory.get(reverse('users:users-register'))
        request.user = self.user
        response = RegisterView.as_view()(request)

        # Check if the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to ensure it goes to the login page
        if response.status_code == 302:
            # Use the client to follow the redirect
            response = self.client.get(response.url)

        # Check if the final response status code after redirect is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_custom_login_view_get(self):
        # Test GET request to custom login view
        request = self.factory.get(reverse('users:login'))
        request.user = self.user  # Set the user attribute on the request
        response = CustomLoginView.as_view()(request)
        # Check if the view returns 200 OK
        self.assertEqual(response.status_code, 200)

    def test_update_user_view_get(self):
        # Test GET request to update_user view
        request = self.factory.get(reverse('users:edit-profile'))
        request.user = self.user  # Set the user attribute on the request
        response = UpdateUserView.as_view()(request)
        # Check if the view returns 200 OK
        self.assertEqual(response.status_code, 200)

    def test_view_user_profile_view(self):
        # Test GET request to view_user_profile view
        request = self.factory.get(reverse('users:view-profile'))
        request.user = self.user  # Set the user attribute on the request
        response = ViewUserProfileView.as_view()(request)
        # Check if the view returns 200 OK
        self.assertEqual(response.status_code, 200)
