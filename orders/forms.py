from django import forms
from django.core.exceptions import ValidationError

from .models import Order


class RadioSelect(forms.RadioSelect):
    input_type = 'radio'


class Select(forms.Select):
    input_type = 'select'


class PlaceOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['street', 'city', 'state',
                  'zipcode', 'mobile', 'payment_method', 'branch']
        widgets = {
            'payment_method': RadioSelect(),
            'branch': Select()
        }

    street = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter street",
            }
        ),
    )

    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter city",
            }
        ),
    )

    state = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter state",
            }
        ),
    )

    zipcode = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter zipcode",
            }
        ),
    )

    mobile = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter mobile",
            }
        ),
    )
