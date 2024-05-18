from django.test import TestCase
from branches.models import Day, Branch


class DayModelTest(TestCase):
    def test_create_day(self):
        day = Day.objects.create(day_of_week='Monday')
        self.assertEqual(day.day_of_week, 'Monday')
        self.assertEqual(str(day), 'Monday')


class BranchModelTest(TestCase):
    def test_create_branch(self):
        branch = Branch.objects.create(
            branch_name='Yummy Food Restaurant - Bukit Bintang',
            branch_address='123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur',
            branch_contact='+60 3-1234 5678'
        )
        self.assertEqual(branch.branch_name,
                         'Yummy Food Restaurant - Bukit Bintang')
        self.assertEqual(branch.branch_address,
                         '123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur')
        self.assertEqual(branch.branch_contact, '+60 3-1234 5678')
        self.assertTrue(branch.is_closed())
        self.assertEqual(str(branch), 'Yummy Food Restaurant - Bukit Bintang')

        # Testing ManyToMany relationship with Day
        day1 = Day.objects.create(day_of_week='Monday')
        day2 = Day.objects.create(day_of_week='Tuesday')
        branch.day.add(day1)
        branch.day.add(day2)
        self.assertEqual(branch.day.count(), 2)
