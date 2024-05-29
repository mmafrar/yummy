from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.ViewDashboardView.as_view(), name='dashboard'),

    path('menus', views.ViewAdminMenu.as_view(), name='menus.index'),
    path('menus/create', views.AddMenuView.as_view(), name='menus.create'),
    path('menus/<int:pk>/edit', views.ViewUpdateMenuView.as_view(), name='menus.edit'),
    path('menus/<int:pk>/delete',
         views.DeleteMenuView.as_view(), name='menus.delete'),

    path('branches', views.ViewAdminBranchs.as_view(), name='branches.index'),
    path('branches/create', views.ViewAddBranchView.as_view(),
         name='branches.create'),
    path('branches/<int:pk>/edit',
         views.ViewUpdateBranchView.as_view(), name='branches.edit'),
    path('branches/<int:branch_id>/edit/opening-hours',
         views.ViewUpdateOpeningHoursView.as_view(), name='branches.edit.opening-hours'),
    path('branches/<int:pk>/delete',
         views.ViewDeleteBranchView.as_view(), name='branches.delete'),

    path('order', views.ViewOrder.as_view(), name='view-order'),
    path('order-details', views.ViewOrderDetails.as_view(),
         name='view-order-details'),
    path('order-status/<int:pk>', views.ViewOrderAfterStatus.as_view(),
         name='order-after-status'),
]
