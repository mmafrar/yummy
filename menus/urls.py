from django.urls import path

from . import views

urlpatterns = [
    path("", views.ViewMenuView.as_view(), name="menu"),
]
