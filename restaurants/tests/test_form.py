from django.test import TestCase
from restaurants.form import AddBranchForm
from restaurants.models import Day


class TestBranchForm(TestCase):
    def test_add_branch_success(self):

        # Create a Day instance with the correct field
        day = Day.objects.create(day_of_week='Monday')

        valid_data = {
            'branch_name': 'Test Branch',
            'branch_address': '123 Test St',
            'branch_contact': '+1234567890',
            'branch_image': None,
            'day': day,
            'opening_time': '09:00:00',
            'closing_time': '17:00:00'
        }

        form = AddBranchForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_add_branch_error(self):

        valid_data = {}

        form = AddBranchForm(data=valid_data)
        self.assertFalse(form.is_valid())