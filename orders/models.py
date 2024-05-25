from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from branches.models import Branch


class PaymentMethod(models.TextChoices):
    CASH = "1", _("Cash")


class OrderStatus(models.TextChoices):
    RECEIVED = "1", _("Received")
    PREPARING = "2", _("Preparing")
    OUT_FOR_DELIVERY = "3", _("Out for Delivery")
    DELIVERED = "4", _("Delivered")


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
        max_length=15, choices=OrderStatus, default=OrderStatus.RECEIVED)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    # menu = models.OneToOneField(Menu, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
