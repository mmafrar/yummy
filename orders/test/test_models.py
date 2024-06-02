from django.test import TestCase
from django.contrib.auth.models import User
from branches.models import Branch
from dashboard.models import Menu
from orders.models import Order, PaymentMethod, OrderStatus


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='pravin', password='pg030399')
        self.branch = Branch.objects.create(branch_name='Pravin Branch', branch_address='Pravin Address', branch_contact='Pravin Contact')
        self.menu = Menu.objects.create(name='Pravin Menu', description='Pravin Description', price=10.00)

    def test_order_creation(self):
        order = Order.objects.create(
            street='Pravin Street',
            city='Klang City',
            state='Selangor',
            zipcode='41200',
            mobile='0124596788',
            total_amount=10.00,
            payment_method=PaymentMethod.CASH,
            user=self.user,
            branch=self.branch,
            menu=self.menu,
        )
        self.assertEqual(order.street, 'Pravin Street')
        self.assertEqual(order.city, 'Klang City')
        self.assertEqual(order.state, 'Selangor')
        self.assertEqual(order.zipcode, '41200')
        self.assertEqual(order.mobile, '0124596788')
        self.assertEqual(order.total_amount, 10.00)
        self.assertEqual(order.payment_method, PaymentMethod.CASH)
        self.assertEqual(order.order_status, OrderStatus.NEW)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.branch, self.branch)
        self.assertEqual(order.menu, self.menu)

    def test_get_name(self):
        order = Order.objects.create(
            street='Pravin Street',
            city='Klang City',
            state='Selangor',
            zipcode='41200',
            mobile='0124596788',
            total_amount=10.00,
            payment_method=PaymentMethod.CASH,
            user=self.user,
            branch=self.branch,
            menu=self.menu,
        )
        self.assertEqual(order.get_name(), f'{self.user.first_name} {self.user.last_name}')

    def test_get_address(self):
        order = Order.objects.create(
            street='Pravin Street',
            city='Klang City',
            state='Selangor',
            zipcode='41200',
            mobile='0124596788',
            total_amount=10.00,
            payment_method=PaymentMethod.CASH,
            user=self.user,
            branch=self.branch,
            menu=self.menu,
        )
        expected_address = 'Pravin Street, Klang City, Selangor, 41200'
        self.assertEqual(order.get_address(), expected_address)
