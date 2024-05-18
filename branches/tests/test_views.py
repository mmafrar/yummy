from django.test import TestCase, RequestFactory
from dashboard.views import ViewAdminBranchs, ViewAddBranchView, ViewUpdateBranchView, ViewDeleteBranchView
from django.contrib import messages
from django.urls import reverse
from branches.models import Branch, Day


class TestAdminBranchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('dashboard:view-admin-branch')

    def test_get_admin_branch_view(self):
        request = self.factory.get(self.url)
        request._messages = messages.storage.default_storage(request)
        response = ViewAdminBranchs.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestAddBranchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('dashboard:add-branch')

    def test_get_add_branch_view(self):
        request = self.factory.get(self.url)
        request._messages = messages.storage.default_storage(request)
        response = ViewAddBranchView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestUpdateBranchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.branch = Branch.objects.create(
            branch_name='Yummy Food Restaurant - Sunway Pyramid',
            branch_address='LG126.A Sunway Pyramid, 3, Jalan PJS 11/15, 47500 Petaling Jaya, Selangor',
            branch_contact='+60 3-1234 2445',
        )
        # Construct the URL pattern with the pk parameter
        self.url = reverse('dashboard:update-branch',
                           kwargs={'pk': self.branch.pk})

    def test_get_update_branch_view(self):
        request = self.factory.get(self.url)
        request._messages = messages.storage.default_storage(request)
        response = ViewUpdateBranchView.as_view()(request, pk=self.branch.pk)
        self.assertEqual(response.status_code, 200)


class TestDeleteBranchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.branch = Branch.objects.create(
            branch_name='Yummy Food Restaurant - Sunway Pyramid',
            branch_address='LG126.A Sunway Pyramid, 3, Jalan PJS 11/15, 47500 Petaling Jaya, Selangor',
            branch_contact='+60 3-1234 2445',
        )
        self.url = reverse('dashboard:delete-branch',
                           kwargs={'pk': self.branch.pk})

    def test_get_delete_branch_view(self):
        request = self.factory.get(self.url)
        request._messages = messages.storage.default_storage(request)
        response = ViewDeleteBranchView.as_view()(request, pk=self.branch.pk)
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/branches')
