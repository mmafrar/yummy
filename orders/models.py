from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from branches.models import Branch
from dashboard.models import Menu


class PaymentMethod(models.TextChoices):
    CASH = "1", _("Cash")


class OrderStatus(models.TextChoices):
    NEW = "1", _("New")
    ACCEPTED = "2", _("Accepted")
    REJECTED = "3", _("Rejected")


class Order(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)

    total_amount = models.FloatField(default=0.00)
    payment_method = models.CharField(
        max_length=15, choices=PaymentMethod, default=PaymentMethod.CASH)
    order_status = models.CharField(
        max_length=15, choices=OrderStatus, default=OrderStatus.NEW)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_address(self):
        return self.street + ', ' + self.city + ', ' + self.state + ', ' + self.zipcode
