from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from dashboard.models import Menu
class ViewMenuView(View):
    
    def get(self,request):
        menus = Menu.objects.all()
        return render(request,"menu.html",{'menus' : menus})
        

