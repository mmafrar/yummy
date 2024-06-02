from django.test import TestCase
from dashboard.models import Menu
from branches.models import Branch
from orders.models import Order, PaymentMethod
from orders.forms import OrderPlaceForm


class OrderPlaceFormTest(TestCase):

    def setUp(self):
        self.branch = Branch.objects.create(branch_name='Pravin Branch', branch_address='pravin Address', branch_contact='Pravin Contact')
        self.menu = Menu.objects.create(name='Test Menu', description='Test Description', price=10.00)

    def test_order_place_form_valid(self):
        form_data = {
            'street': 'Pravin Street',
            'city': 'Klang City',
            'state': ' Selangor',
            'zipcode': '41200',
            'mobile': '0124596788',
            'payment_method': PaymentMethod.CASH,
            'total_amount': 10.00,
            'branch': self.branch.id,
            'menu': self.menu.id,
        }
        form = OrderPlaceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_place_form_invalid(self):
        form_data = {
            'street': 'Pravin Street',
            'city': 'Klang City',
            'state': ' Selangor',
            'zipcode': '41200',
            'mobile': '',  
            'payment_method': PaymentMethod.CASH,
            'total_amount': 10.00,
            'branch': self.branch.id,
            'menu': self.menu.id,
        }
        form = OrderPlaceForm(data=form_data)
        self.assertFalse(form.is_valid())
