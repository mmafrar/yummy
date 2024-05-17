from django.test import TestCase
from restaurants.models import Day, Branch

class DayModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create Day objects for testing
        Day.objects.create(day_of_week='Monday')
        Day.objects.create(day_of_week='Tuesday')

    def test_day_of_week_label(self):
        day = Day.objects.get(day_of_week='Monday')
        field_label = day._meta.get_field('day_of_week').verbose_name
        self.assertEqual(field_label, 'day of week')

    def test_day_of_week_max_length(self):
        day = Day.objects.get(day_of_week='Monday')
        max_length = day._meta.get_field('day_of_week').max_length
        self.assertEqual(max_length, 150)


class BranchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        day = Day.objects.create(day_of_week='Monday')

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


 