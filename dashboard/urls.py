from django.urls import path

from .views import ContactAdminView, ContactDetailView
from .views import DashboardAdminView, OrderAdminView, OrderDetailView
from .views import MenuAdminView, MenuCreateView, MenuEditView, MenuDeleteView
from .views import BranchAdminView, BranchCreateView, BranchEditView, BranchEditOpeningHoursView, BranchDeleteView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardAdminView.as_view(), name='dashboard'),

    path('menus', MenuAdminView.as_view(), name='menus.index'),
    path('menus/create', MenuCreateView.as_view(), name='menus.create'),
    path('menus/<int:pk>/edit', MenuEditView.as_view(), name='menus.edit'),
    path('menus/<int:pk>/delete', MenuDeleteView.as_view(), name='menus.delete'),

    path('branches', BranchAdminView.as_view(), name='branches.index'),
    path('branches/create', BranchCreateView.as_view(), name='branches.create'),
    path('branches/<int:pk>/edit', BranchEditView.as_view(), name='branches.edit'),
    path('branches/<int:branch_id>/edit/opening-hours',
         BranchEditOpeningHoursView.as_view(), name='branches.edit.opening-hours'),
    path('branches/<int:pk>/delete',
         BranchDeleteView.as_view(), name='branches.delete'),

    path('orders', OrderAdminView.as_view(), name='orders.index'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='orders.show'),

    path('contacts', ContactAdminView.as_view(), name='contacts.index'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='contacts.show'),
]
