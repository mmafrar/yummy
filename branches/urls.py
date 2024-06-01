from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [
    path('', views.ViewBranchesView.as_view(), name='branch'),
]
