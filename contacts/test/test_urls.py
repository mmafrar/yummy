# from django.test import TestCase

# # Create your tests here.
# class TestUrls (TestCase):

#     def test_list_url(self):
#         assert 1==2

from django.test import TestCase
from django.urls import reverse, resolve
from contacts.views import ViewContactView, ViewAbouttView

# Create your tests here.
class TestUrls_contact_us(TestCase):

    # Checks if the URL for the "view-contact" view resolves correctly   
    def test_view_contact_url_resolves(self):
        url = reverse('contacts:view-contact')
        self.assertEqual(resolve(url).func.view_class, ViewContactView)

    # Checks that the URL for the "view-about" view resolves correctly
    def test_view_about_url_resolves(self):
        url = reverse('contacts:view-about')
        self.assertEqual(resolve(url).func.view_class, ViewAbouttView)

    # Checks if the correct template is used when accessing the view-contact URL
    def test_view_contact_template(self):
        response = self.client.get(reverse('contacts:view-contact'))
        self.assertTemplateUsed(response, 'contact.html') 

    # Checks if the correct template is used when accessing the view-about URL
    def test_view_about_template(self):
        response = self.client.get(reverse('contacts:view-about'))
        self.assertTemplateUsed(response, 'about.html')  