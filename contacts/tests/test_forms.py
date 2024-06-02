from django.test import TestCase
from contacts.forms import ContactForm
from contacts.models import Contact


class TestContactForm(TestCase):

    def test_contact_form_valid(self):
        # Positive scenario data with actual users
        form_data = {
            'name': 'Mashkur',
            'email': 'Mash@hotmail.com',
            'subject': 'Complaint',
            'message': 'Less menu items'
        }

        # With valid data
        form = ContactForm(data=form_data)

        # Form is valid
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_missing_email(self):
        # Negative scenario data with actual users
        invalid_data = {
            'name': 'Mashkur',
            'email': '',
            'subject': 'Complaint',
            'message': 'Less menu items'
        }

        # With invalid data missing email
        form = ContactForm(data=invalid_data)

        # Form is invalid
        self.assertFalse(form.is_valid())

    def test_contact_form_invalid_missing_name(self):
        # Invalid data
        invalid_data = {
            'name': '',
            'email': 'Mash@hotmail.com',
            'subject': 'Complaint',
            'message': 'Less menu items'
        }

        # With invalid data missing name
        form = ContactForm(data=invalid_data)

        # Form is invalid
        self.assertFalse(form.is_valid())
