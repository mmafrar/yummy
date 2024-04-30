from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

class ViewMenuView(View):
    
    def get(self,request):
        return render(request,"blog/blog-menu.html")
        
    def post(self,request):
        pass
