from django.shortcuts import render
from django.views import View


class ViewUserProfileView(View):
    
    def get(self,request):
        return render(request,"user-profile.html")

class ViewEditProfileView(View):
    
    def get(self,request):
        return render(request,"edit-profile.html")
        