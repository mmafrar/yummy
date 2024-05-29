from django.test import TestCase
from decimal import Decimal
from ..models import Menu


class MenuModelTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            name='Starter Salad',
            description='Fresh greens with vinaigrette dressing',
            image='menus/starter_salad.jpg',
            price=Decimal('12.99'),
            category=Menu.SALADS
        )

    def test_menu_creation(self):
        menu_item = Menu.objects.get(name='Starter Salad')
        self.assertEqual(menu_item.price, Decimal('12.99'))

    def test_menu_update(self):
        menu_item = Menu.objects.get(name='Starter Salad')
        menu_item.price = Decimal('15.99')
        menu_item.save()
        updated_menu_item = Menu.objects.get(name='Starter Salad')
        self.assertEqual(updated_menu_item.price, Decimal('15.99'))

    def test_menu_delete(self):
        menu_item = Menu.objects.get(name='Starter Salad')
        menu_item.delete()
        with self.assertRaises(Menu.DoesNotExist):
            Menu.objects.get(name='Starter Salad')
