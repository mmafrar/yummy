from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.ViewOrderFormView.as_view(), name="view-order-form"),
]
