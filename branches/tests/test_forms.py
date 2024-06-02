from django.test import TestCase
from branches.forms import BranchForm, OpeningHourForm


class BranchFormTest(TestCase):
    def test_branch_form_valid_data(self):
        form = BranchForm(data={
            'branch_name': 'Yummy Food Restaurant - Sunway Pyramid',
            'branch_address': 'LG126.A Sunway Pyramid, 3, Jalan PJS 11/15, 47500 Petaling Jaya, Selangor',
            'branch_contact': '+60 3-1234 2445'
        })
        self.assertTrue(form.is_valid())

    def test_branch_form_invalid_data(self):
        form = BranchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class OpeningHourFormTest(TestCase):
    def test_opening_hour_form_valid_data(self):
        form = OpeningHourForm(data={
            'day': 'MO',
            'open_time': '09:00',
            'close_time': '17:00'
        })
        self.assertTrue(form.is_valid())

    def test_opening_hour_form_invalid_data(self):
        form = OpeningHourForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
