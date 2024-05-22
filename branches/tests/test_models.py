from django.core.exceptions import ValidationError
from django.test import TestCase
from branches.models import Branch, OpeningHour


class BranchModelTestCase(TestCase):
    def setUp(self):
        self.branch = Branch.objects.create(
            branch_name="Yummy Food Restaurant - Bukit Bintang",
            branch_address="123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur",
            branch_contact="+60 3-1234 5678"
        )

    def test_branch_creation(self):
        self.assertEqual(self.branch.branch_name,
                         "Yummy Food Restaurant - Bukit Bintang")
        self.assertEqual(self.branch.branch_address,
                         "123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur")
        self.assertEqual(self.branch.branch_contact, "+60 3-1234 5678")

    def test_branch_creation_error(self):
        obj = Branch.objects.create(
            branch_address="123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur",
            branch_contact="+60 3-1234 5678"
        )
        self.assertRaises(ValidationError, obj.full_clean)


class OpeningHourModelTestCase(TestCase):
    def setUp(self):
        self.branch = Branch.objects.create(
            branch_name="Yummy Food Restaurant - Bukit Bintang",
            branch_address="123 Jalan Bukit Bintang, Bukit Bintang, 55100 Kuala Lumpur",
            branch_contact="+60 3-1234 5678"
        )
        self.opening_hour = OpeningHour.objects.create(
            branch=self.branch,
            day="MO",
            open_time="08:00",
            close_time="17:00"
        )

    def test_opening_hour_creation(self):
        self.assertEqual(self.opening_hour.branch, self.branch)
        self.assertEqual(self.opening_hour.day, "MO")
        self.assertEqual(
            self.opening_hour.open_time, "08:00")
        self.assertEqual(
            self.opening_hour.close_time, "17:00")

    def test_opening_hour_string_representation(self):
        expected_string = "Yummy Food Restaurant - Bukit Bintang - Monday: 08:00 to 17:00"
        self.assertEqual(str(self.opening_hour), expected_string)

    def test_unique_opening_hours(self):
        with self.assertRaises(Exception):
            OpeningHour.objects.create(
                branch=self.branch,
                day="MO",
                open_time="09:00",
                close_time="18:00"
            )
