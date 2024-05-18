from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.ViewDashboardView.as_view(), name='view-dashboard'),

    path('branches', views.ViewAdminBranchs.as_view(), name='view-admin-branch'),
    path('branches/add', views.ViewAddBranchView.as_view(), name='add-branch'),
    path('branches/update/<int:pk>',
         views.ViewUpdateBranchView.as_view(), name='update-branch'),
    path('branches/delete/<int:pk>',
         views.ViewDeleteBranchView.as_view(), name='delete-branch'),

    path('order', views.ViewOrder.as_view(), name='view-order'),
    path('order-details', views.ViewOrderDetails.as_view(),
         name='view-order-details'),
    path('order-status/<int:pk>', views.ViewOrderAfterStatus.as_view(),
         name='order-after-status'),

    path('menu', views.ViewAdminMenu.as_view(), name='view-admin-menu'),
    path('add-menu', views.ViewAddMenuView.as_view(), name='add-menu'),
    path('update-menu/<int:pk>',
         views.ViewUpdateMenuView.as_view(), name='update-menu'),
]
