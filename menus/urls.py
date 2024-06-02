from django.urls import path

from .views import MenuIndexView

urlpatterns = [
    path("", MenuIndexView.as_view(), name="menu"),
]
