from django.views import View
from django.shortcuts import render

from dashboard.models import Menu


class MenuIndexView(View):

    def get(self, request):
        menus = Menu.objects.all()
        return render(request, "menu-index.html", {'menus': menus})
