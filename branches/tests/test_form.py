from django.test import TestCase
from branches.form import AddBranchForm
from branches.models import Day


class TestBranchForm(TestCase):
    def test_add_branch_success(self):

        valid_data = {
            'branch_name': 'Test Branch',
            'branch_address': '123 Test St',
            'branch_contact': '+1234567890',
            'branch_image': None,
        }

        form = AddBranchForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_add_branch_error(self):

        valid_data = {}

        form = AddBranchForm(data=valid_data)
        self.assertFalse(form.is_valid())
