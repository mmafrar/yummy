from django.urls import path

from .views import OrderPlaceView

app_name = 'orders'

urlpatterns = [
    path("", OrderPlaceView.as_view(), name="order"),
]
