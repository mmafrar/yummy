from django.views import View
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PlaceOrderForm


class PlaceOrderView(LoginRequiredMixin, View):

    login_url = "../users/login"
    redirect_field_name = "redirect_to"

    def get(self, request):
        menu = {'id': 1, 'name': 'Caesar Salad',
                'category': 'Salad', 'amount': '10.99'}

        form = PlaceOrderForm()
        args = {'form': form, 'menu': menu}

        return render(request, "place-order.html", args)

    def post(self, request):
        form = PlaceOrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return render(request, "confirm-order.html")

        else:
            raise ValidationError()
