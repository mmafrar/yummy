from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ViewContactView.as_view(), name='contact'),
    path('about', views.ViewAbouttView.as_view(), name='about'),
]
