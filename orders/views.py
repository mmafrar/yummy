from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderPlaceForm
from dashboard.models import Menu


class OrderPlaceView(LoginRequiredMixin, View):

    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = OrderPlaceForm()
        menu_id = request.GET.get('menu_id')
        menu = Menu.objects.get(pk=menu_id)
        return render(request, 'order-place.html', {'form': form, 'menu': menu})

    def post(self, request):
        form = OrderPlaceForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return render(request, 'order-confirm.html')
        else:
            return render(request, 'order-place.html', {'form': form, 'menu': form.menu})
