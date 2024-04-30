from django.shortcuts import render
from django.views import View


class ViewResturantView(View):
    
    def get(self,request):
        return render(request,"branches.html")
