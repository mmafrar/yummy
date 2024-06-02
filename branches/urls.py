from django.urls import path

from .views import BranchIndexView

app_name = 'branches'

urlpatterns = [
    path('', BranchIndexView.as_view(), name='branch'),
]
