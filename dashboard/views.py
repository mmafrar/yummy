from django.shortcuts import render, redirect
from django.views import View


class ViewDashboardView(View):

    def get(self, request):
        if request.user.is_authenticated and self.request.user.is_superuser:
            return render(request, "dashboard.html")
        return redirect('users:login')


class ViewAdminMenu(View):

    def get(self, request):
        return render(request, "menu/admin-menu.html")


class ViewAddMenuView(View):

    def get(self, request):
        return render(request, "menu/add-menu.html")


class ViewUpdateMenuView(View):

    def get(self, request, pk):
        return render(request, "menu/update-menu.html")


class ViewAdminBranchs(View):

    def get(self, request):
        return render(request, "branch/admin-branch.html")


class ViewAddBranchView(View):

    def get(self, request):
        return render(request, "branch/add-branch.html")


class ViewUpdateBranchView(View):

    def get(self, request, pk):
        return render(request, "branch/update-branch.html")


class ViewOrder(View):

    def get(self, request):
        return render(request, "order/order-management.html")


class ViewOrderDetails(View):

    def get(self, request):
        return render(request, "order/order-details.html")


class ViewOrderAfterStatus(View):

    def get(self, request, pk):
        return render(request, "order/order-after-status.html")
