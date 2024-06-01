from django import forms

from dashboard.models import Menu
from branches.models import Branch
from .models import Order, PaymentMethod


class OrderPlaceForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['street', 'city', 'state', 'zipcode', 'mobile',
                  'payment_method', 'total_amount', 'branch', 'menu']

    street = forms.CharField(
        required=True,
        max_length=50,
        label='Street Address',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter street address",
            }
        ),
    )

    city = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter city",
            }
        ),
    )

    state = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter state",
            }
        ),
    )

    zipcode = forms.CharField(
        required=True,
        max_length=15,
        label='ZIP Code',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter ZIP code",
            }
        ),
    )

    mobile = forms.CharField(
        required=True,
        max_length=15,
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }
        ),
    )

    total_amount = forms.FloatField(
        required=True,
        widget=forms.HiddenInput(),
    )

    payment_method = forms.ChoiceField(
        required=True,
        initial=PaymentMethod.CASH,
        choices=PaymentMethod.choices,
        widget=forms.RadioSelect(),
    )

    branch = forms.ModelChoiceField(
        required=True,
        empty_label='Select branch',
        queryset=Branch.objects.all(),
        label='Select Restaurant Branch',
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    menu = forms.ModelChoiceField(
        required=True,
        empty_label='Select menu',
        queryset=Menu.objects.all(),
        label='Select Menu',
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )
