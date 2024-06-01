from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderPlaceForm
from dashboard.models import Menu


class OrderPlaceView(LoginRequiredMixin, View):

    login_url = "../users/login"
    redirect_field_name = "redirect_to"

    def get(self, request):
        form = OrderPlaceForm()
        menu_id = request.GET.get('menu_id')
        menu = Menu.objects.get(pk=menu_id)

        args = {'form': form, 'menu': menu}
        return render(request, "order-place.html", args)

    def post(self, request):
        form = OrderPlaceForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return render(request, "order-confirm.html")

        else:
            args = {'form': form, 'menu': form.menu}
            return render(request, "order-place.html", args)
