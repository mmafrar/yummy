from django.shortcuts import render
from django.views import View


class ViewContactView(View):

    def get(self, request):
        return render(request, "contact.html")


class ViewAbouttView(View):

    def get(self, request):
        return render(request, "about.html")
