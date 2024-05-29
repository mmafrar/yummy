from django.test import TestCase
from dashboard.forms import MenuForm
from django.core.files.uploadedfile import SimpleUploadedFile


class MenuFormTest(TestCase):

    def test_menu_form_valid_data(self):
        # Prepare test data
        image_data = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x05\x00\xFF\x00\x00\x00\x00\x00\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B'
        image = SimpleUploadedFile(
            'test_image.gif', image_data, content_type='image/gif')

        form_data = {
            'name': 'Test Menu',
            'description': 'This is a test menu item',
            'image': image,
            'price': '15.99',
            'category': 'Starters'
        }

        form = MenuForm(data=form_data, files={'image': image})
        self.assertTrue(form.is_valid(), form.errors.as_data())

        def test_menu_form_invalid_data(self):

            # Test with missing required fields
            form_missing_data = MenuForm(data={})
            self.assertFalse(form_missing_data.is_valid())
            self.assertEqual(len(form_missing_data.errors), 4)

        # Test with invalid price (non-numeric)
        form_invalid_price = MenuForm(data={
            'name': 'Invalid Menu',
            'description': 'Invalid menu without price',
            'image': '',
            'price': 'InvalidPrice',
            'category': 'Starters'
        })

        self.assertFalse(form_invalid_price.is_valid())
        self.assertIn('price', form_invalid_price.errors)

        # Test with missing image
        form_missing_image = MenuForm(data={
            'name': 'Menu without Image',
            'description': 'This menu does not have an image',
            'price': 12.50,
            'category': 'Salads'
        })

        self.assertFalse(form_missing_image.is_valid())
        self.assertIn('image', form_missing_image.errors)
