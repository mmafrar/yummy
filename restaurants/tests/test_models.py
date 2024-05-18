from django.test import TestCase
from restaurants.models import Day, Branch


class BranchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        day = Day.MONDAY

        Branch.objects.create(
            branch_name='Test Branch',
            branch_address='123 Test St',
            branch_contact='+1234567890',
            opening_time='09:00:00',
            closing_time='17:00:00',
            day=day
        )

    def test_branch_name_label(self):
        branch = Branch.objects.get(branch_name='Test Branch')
        field_label = branch._meta.get_field('branch_name').verbose_name
        self.assertEqual(field_label, 'branch name')
