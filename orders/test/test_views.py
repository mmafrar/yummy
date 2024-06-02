from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from dashboard.models import Menu
from orders.models import Order
from orders.forms import OrderPlaceForm

class OrderPlaceViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='pravin', password='pg030399')
        self.menu = Menu.objects.create(name='Pravin Menu', description='Pravin Description', price=10.00)
        self.client = Client()
        self.client.login(username='pravin', password='pg030399')

    def test_get_order_place_view(self):
        response = self.client.get(reverse('orders:order') + f'?menu_id={self.menu.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order-place.html')
        self.assertIsInstance(response.context['form'], OrderPlaceForm)
        self.assertEqual(response.context['form'].fields['menu'].queryset.count(), 1) 
        self.assertEqual(response.context['menu'], self.menu)

def test_post_order_place_view_invalid(self):
    form_data = {
        'street': 'Pravin Street',
        'city': 'Klang City',
        'state': ' Selangor',
        'zipcode': '41200',
        'mobile': '0124596788',
        'payment_method': 'CASH',
        'total_amount': 10.00,
        'branch': self.menu.branch_id, 
        'menu': self.menu.id,
    }
    response = self.client.post(reverse('orders:order'), data=form_data)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'order-place.html')
    self.assertTrue(response.context['form'].errors)
    self.assertFalse(Order.objects.filter(user=self.user, menu=self.menu).exists())

def test_post_order_place_view_valid(self):
    form_data = {
        'street': 'Pravin Street',
        'city': 'Klang City',
        'state': ' Selangor',
        'zipcode': '41200',
        'mobile': '0124596788',
        'payment_method': 'CASH',
        'total_amount': 10.00,
        'branch': self.menu.branch_id, 
        'menu': self.menu.id,
    }
    response = self.client.post(reverse('orders:order'), data=form_data)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'order-confirm.html')
    self.assertTrue(Order.objects.filter(user=self.user, menu=self.menu).exists())
