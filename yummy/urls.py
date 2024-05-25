"""
URL configuration for yummy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import include, path

from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('branches/', include(('branches.urls', 'branches'), namespace='branches')),
    path('menus/', include(('menus.urls', 'menus'), namespace='menus')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('contacts/', include(('contacts.urls', 'contacts'), namespace='contacts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
