from django.shortcuts import render
from django.views import View



class ViewOrderFormView(View):
    
    def get(self,request):
        return render(request,"order-now.html")
        

class OrderConfirmationView(View):
    
    def get(self,request):
        return render(request,"order-confirmation.html")
        
   
