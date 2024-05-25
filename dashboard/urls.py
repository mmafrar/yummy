from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', views.ViewDashboardView.as_view(), name='view-dashboard'),
    path('menu', views.ViewAdminMenu.as_view(), name='view-admin-menu'),
    path('add-menu', views.ViewAddMenuView.as_view(), name='add-menu'),
    path('update-menu/<int:pk>',
         views.ViewUpdateMenuView.as_view(), name='update-menu'),
    path('branches', views.ViewAdminBranchs.as_view(), name='view-admin-branch'),
    path('add-branch', views.ViewAddBranchView.as_view(), name='add-branch'),
    path('update-branch/<int:pk>',
         views.ViewUpdateBranchView.as_view(), name='update-branch'),
    path('update-branch/opening-hours/<int:branch_id>',
         views.ViewUpdateOpeningHoursView.as_view(), name='update-opening-hours'),
    path('delete-branch/<int:pk>',
         views.ViewDeleteBranchView.as_view(), name='delete-branch'),
    path('order', views.ViewOrder.as_view(), name='view-order'),
    path('order-details', views.ViewOrderDetails.as_view(),
         name='view-order-details'),
    path('order-status/<int:pk>', views.ViewOrderAfterStatus.as_view(),
         name='order-after-status'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
