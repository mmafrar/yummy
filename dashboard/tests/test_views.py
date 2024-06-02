from unittest.mock import patch
from django.urls import reverse
from django.test import TestCase
from django.http import HttpResponseRedirect
from django.test import Client, TestCase, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages.storage.fallback import FallbackStorage

from dashboard.models import Menu
from branches.models import Branch
from dashboard.views import BranchCreateView


class BranchCreateViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_branch_view(self):
        request = self.factory.get('dashboard:branches.index')
        request.user = None  # Set user later
        response = BranchCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_branch_post_valid_data(self):
        request = self.factory.post('dashboard:branches.create', {
            'branch_name': 'Yummy Food Restaurant - Pavilion Bukit Jalil'})
        request.user = None  # set user later
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = BranchCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Branch.objects.count(), 0)

    def test_branch_post_invalid_data(self):
        request = self.factory.post('dashboard:branches.create', {})
        request.user = None  # set user later
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = BranchCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Branch.objects.count(), 0)


class MenuViewTest(TestCase):
    def setUp(self):

        self.menu1 = Menu.objects.create(
            name='Starter 1',
            description='Description for Starter 1',
            image=SimpleUploadedFile(
                'starter1.jpg', b'content', content_type='image/jpeg'),
            price=10.99,
            category='Starters'
        )
        self.menu2 = Menu.objects.create(
            name='Salad 1',
            description='Description for Salad 1',
            image=SimpleUploadedFile(
                'salad1.jpg', b'content', content_type='image/jpeg'),
            price=12.99,
            category='Salads'
        )

    def test_menu_view(self):
        # Simulate a GET request to the menu view
        response = self.client.get(reverse('menus:menu'))

        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is correct
        self.assertTemplateUsed(response, 'menu-index.html')

        # Check if menu items are present in the context
        self.assertIn('menus', response.context)

        # Check if menu items are displayed correctly in the rendered HTML
        self.assertContains(response, self.menu1.name)
        self.assertContains(response, self.menu2.name)
