from unittest.mock import patch
from django.http import HttpResponseRedirect
from django.test import Client, TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import reverse
from branches.models import Branch
from dashboard.views import ViewAddBranchView


class ViewAddBranchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_branch_view(self):
        request = self.factory.get('dashboard:view-admin-branch')
        request.user = None  # Set user later
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_branch_post_valid_data(self):
        request = self.factory.post('dashboard:add-branch', {
            'branch_name': 'Yummy Food Restaurant - Pavilion Bukit Jalil'})
        request.user = None  # set user later
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Branch.objects.count(), 0)

    def test_branch_post_invalid_data(self):
        request = self.factory.post('dashboard:add-branch', {})
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

        url = reverse('dashboard:delete-branch', kwargs={'pk': branch.pk})

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
        self.assertEqual(response.url, reverse('dashboard:view-admin-branch'))
