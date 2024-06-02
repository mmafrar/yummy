from django.urls import path

from .views import ContactIndexView, ContactAboutView

app_name = 'contacts'

urlpatterns = [
    path('', ContactIndexView.as_view(), name='contact'),
    path('about', ContactAboutView.as_view(), name='about'),
]
