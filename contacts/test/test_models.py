from django.test import TestCase
from contacts.models import Contact

class TestContactModel(TestCase):

    def test_contact_creation(self):
        # Verifying input field by creating a contact
        contact = Contact.objects.create(
            name='Pravin Kannappan',
            email='irpravin@gmail.com',
            subject='Enquiry',
            message='How long does it take for delivery'
        )

        # Verify if the contact was created successfully
        self.assertIsNotNone(contact)
        self.assertEqual(contact.name, 'Pravin Kannappan')
        self.assertEqual(contact.email, 'irpravin@gmail.com')
        self.assertEqual(contact.subject, 'Enquiry')
        self.assertEqual(contact.message, 'How long does it take for delivery')

    def test_contact_str_representation(self):
        # Verifying input field by creating a contact
        contact = Contact.objects.create(
            name='RajiniKanth',
            email='RajiniKanth@gmail.com',
            subject='Enquiry',
            message='How long does it take for delivery'
        )

        # Check if the __str__ method returns the expected string representation
        self.assertEqual(str(contact), 'RajiniKanth')