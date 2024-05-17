from django.shortcuts import render, redirect
from django.views import View
from .models import Branch



class ViewResturantView(View):
    
    def get(self,request):
        all_branches = Branch.objects.all()
        context = {'all_branches': all_branches}
        return render(request,"branches.html", context)
  