from django.views import View
from django.shortcuts import render


class YummyIndexView(View):

    def get(self, request):
        return render(request, "yummy-index.html")
