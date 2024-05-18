from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from branches.form import AddBranchForm
from branches.models import Branch


class ViewDashboardView(View):

    def get(self, request):
        return render(request, "dashboard.html")


class ViewAdminMenu(View):

    def get(self, request):
        return render(request, "menu/admin-menu.html")


class ViewAddMenuView(View):

    def get(self, request):
        return render(request, "menu/add-menu.html")


class ViewUpdateMenuView(View):

    def get(self, request, pk):
        return render(request, "menu/update-menu.html")

# Added by Hanifah


class ViewAdminBranchs(View):

    def get(self, request):
        all_branches = Branch.objects.all().order_by('-id')
        context = {'all_branches': all_branches}
        return render(request, "branch/admin-branch.html", context)

# Added by Hanifah
# @login_required


class ViewAddBranchView(View):
    # Call Add Branch from Restaurants App
    def post(self, request):
        form = AddBranchForm(request.POST, request.FILES)
        if form.is_valid():
            branch_name = form.cleaned_data['branch_name']
            if Branch.objects.filter(branch_name=branch_name).exists():
                return render(request, 'branch/add-branch.html', {'form': form, 'error_message': 'Branch already exists.'})
            else:
                form.save()
                messages.success(request, 'Branch added successfully')
                return redirect('dashboard:view-admin-branch')
        context = {'form': form}
        return render(request, 'branch/add-branch.html', context)

    def get(self, request):
        form = AddBranchForm()
        context = {'form': form}
        return render(request, 'branch/add-branch.html', context)


# Added by Hanifah
# @login_required
class ViewUpdateBranchView(View):
    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        form = AddBranchForm(instance=branch)
        return render(request, 'branch/update-branch.html', {'form': form})

    def post(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        form = AddBranchForm(request.POST, request.FILES, instance=branch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Branch updated successfully')
            return redirect('dashboard:view-admin-branch')
        return render(request, 'branch/update-branch.html', {'form': form})

# Added by Hanifah
# @login_required


class ViewDeleteBranchView(View):
    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
        messages.success(request, 'Branch deleted sucessfully')
        return redirect('dashboard:view-admin-branch')


class ViewOrder(View):

    def get(self, request):
        return render(request, "order/order-management.html")


class ViewOrderDetails(View):

    def get(self, request):
        return render(request, "order/order-details.html")


class ViewOrderAfterStatus(View):

    def get(self, request, pk):
        return render(request, "order/order-after-status.html")
