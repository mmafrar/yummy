from unittest.mock import patch
from django.urls import reverse
from django.test import TestCase
from django.http import HttpResponseRedirect
from django.test import Client, TestCase, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages.storage.fallback import FallbackStorage

from dashboard.models import Menu
from branches.models import Branch
from dashboard.views import ViewAddBranchView


class ViewAddBranchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_branch_view(self):
        request = self.factory.get('dashboard:branches.index')
        request.user = None  # Set user later
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_branch_post_valid_data(self):
        request = self.factory.post('dashboard:branches.create', {
            'branch_name': 'Yummy Food Restaurant - Pavilion Bukit Jalil'})
        request.user = None  # set user later
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Branch.objects.count(), 0)

    def test_branch_post_invalid_data(self):
        request = self.factory.post('dashboard:branches.create', {})
        request.user = None  # set user later
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Branch.objects.count(), 0)


class ViewDeleteBranchViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('django.contrib.messages.success')
    def test_get(self, mock_messages_success):
        branch = Branch.objects.create(
            branch_name="Yummy Food Restaurant - IOI City Mall",
            branch_address="LG-239, Lower Ground Floor, IOI City Mall, Lebuh IRC, IOI Resort City, 62502 Putrajaya",
            branch_contact="+60 3-4258 8889")

        url = reverse('dashboard:branches.delete', kwargs={'pk': branch.pk})

        # Call view function
        response = self.client.get(url)

        # Check if the branch is deleted
        with self.assertRaises(Branch.DoesNotExist):
            Branch.objects.get(pk=branch.pk)

        # Check if success message is called
        mock_messages_success.assert_called_once_with(
            response.wsgi_request, 'Branch deleted sucessfully')

        # Check if redirect happens
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('dashboard:branches.index'))


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
        self.assertTemplateUsed(response, 'menu.html')

        # Check if menu items are present in the context
        self.assertIn('menus', response.context)

        # Check if menu items are displayed correctly in the rendered HTML
        self.assertContains(response, self.menu1.name)
        self.assertContains(response, self.menu2.name)
