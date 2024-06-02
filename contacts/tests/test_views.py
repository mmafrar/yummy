from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from contacts.forms import ContactForm
from contacts.models import Contact


class TestContactView(TestCase):

    def setUp(self):
        self.client = Client()
        self.view_contact_url = reverse('contacts:contact')
        self.view_about_url = reverse('contacts:about')
        self.valid_form_data = {
            'name': 'Pravin',
            'email': 'irpravin@gmail.com',
            'subject': 'Compliment',
            'message': 'Food was good'
        }

    def test_view_contact_get(self):
        # Verify GET request
        response = self.client.get(self.view_contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-index.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_view_contact_post_valid_form(self):
        # Verify valid POST request
        response = self.client.post(
            self.view_contact_url, data=self.valid_form_data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, self.view_contact_url)

        # Verify that the form was saved upon sending
        self.assertEqual(Contact.objects.count(), 1)

        # Verify if the an email was sent after post request
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Compliment')

    def test_view_contact_post_invalid_form(self):
        # Verify if invalid POST request (missing required fields)
        invalid_data = self.valid_form_data.copy()
        invalid_data['email'] = ''  # Email is required (Empty string)
        response = self.client.post(self.view_contact_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-index.html')
        self.assertFalse(response.context['form'].is_valid())
        # No contact should be saved
        self.assertEqual(Contact.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)  # No email should be sent


class TestAboutView(TestCase):
    # Verifying by setting up client defining URL for the about view
    def setUp(self):
        self.client = Client()
        self.view_about_url = reverse('contacts:about')
    # Verify the response status code is 200 (indicating success), and verifies that the correct template

    def test_view_about_get(self):
        response = self.client.get(self.view_about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-about.html')
