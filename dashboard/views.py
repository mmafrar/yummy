from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from branches.models import Branch, OpeningHour
from branches.form import BranchForm, OpeningHourFormSet


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


class ViewOrder(View):

    def get(self, request):
        return render(request, "order/order-management.html")


class ViewOrderDetails(View):

    def get(self, request):
        return render(request, "order/order-details.html")


class ViewOrderAfterStatus(View):

    def get(self, request, pk):
        return render(request, "order/order-after-status.html")


class ViewAdminBranchs(View):

    def get(self, request):
        all_branches = Branch.objects.all().order_by('-id')
        context = {'all_branches': all_branches}
        return render(request, "branch/admin-branch.html", context)


class ViewAddBranchView(View):
    def get(self, request):
        branch_form = BranchForm()
        opening_hour_formset = OpeningHourFormSet(
            queryset=OpeningHour.objects.none())
        return render(request, 'branch/add-branch.html', {'branch_form': branch_form, 'opening_hour_formset': opening_hour_formset})

    def post(self, request):
        branch_form = BranchForm(request.POST, request.FILES)
        opening_hour_formset = OpeningHourFormSet(request.POST)

        if branch_form.is_valid() and opening_hour_formset.is_valid():
            branch_name = branch_form.cleaned_data['branch_name']
            if Branch.objects.filter(branch_name=branch_name).exists():
                messages.error(request, 'Branch already exists.')
                return render(request, 'branch/add-branch.html', {
                    'branch_form': branch_form,
                    'opening_hour_formset': opening_hour_formset, })
            else:
                days = set()
                for form in opening_hour_formset.forms:
                    day = form.cleaned_data.get('day')
                    if day in days:
                        messages.error(
                            request, 'Duplicate day found in opening hours.')
                        return render(request, 'branch/add-branch.html', {
                            'branch_form': branch_form,
                            'opening_hour_formset': opening_hour_formset, })
                    days.add(day)

                branch_instance = branch_form.save()
                opening_hour_instances = opening_hour_formset.save(
                    commit=False)
                for opening_hour_instance in opening_hour_instances:
                    opening_hour_instance.branch = branch_instance
                    opening_hour_instance.save()
                messages.success(request, 'Branch added successfully')
                return redirect('dashboard:view-admin-branch')
        return render(request, 'branch/add-branch.html', {
            'branch_form': branch_form,
            'opening_hour_formset': opening_hour_formset})


class ViewUpdateBranchView(View):
    def get(self, request, pk):
        branch_instance = get_object_or_404(Branch, pk=pk)
        branch_form = BranchForm(instance=branch_instance)
        return render(request, 'branch/update-branch.html', {
            'branch_form': branch_form,
            'branch_id': pk
        })

    def post(self, request, pk):
        branch_instance = get_object_or_404(Branch, pk=pk)
        branch_form = BranchForm(
            request.POST, request.FILES, instance=branch_instance)

        if branch_form.is_valid():
            branch_name = branch_form.cleaned_data['branch_name']
            if Branch.objects.filter(branch_name=branch_name).exclude(pk=pk).exists():
                messages.error(request, 'Branch already exists.')
            else:

                branch_instance = branch_form.save()
                messages.success(request, 'Branch updated successfully')
                return redirect('dashboard:view-admin-branch')

        return render(request, 'branch/update-branch.html', {
            'branch_form': branch_form,
            'branch_id': pk
        })


class ViewUpdateOpeningHoursView(View):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        opening_hours = OpeningHour.objects.filter(branch=branch)
        opening_hour_formset = OpeningHourFormSet(queryset=opening_hours)
        return render(request, 'branch/update-opening-hours.html', {
            'branch': branch,
            'opening_hour_formset': opening_hour_formset,
        })

    def post(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        opening_hours = OpeningHour.objects.filter(branch=branch)
        opening_hour_formset = OpeningHourFormSet(
            request.POST, queryset=opening_hours)

        if opening_hour_formset.is_valid():
            # Proceed with saving the formset if it's valid
            opening_hour_instances = opening_hour_formset.save(commit=False)
            for opening_hour_instance in opening_hour_instances:
                opening_hour_instance.branch = branch  # Set the branch before saving
                opening_hour_instance.save()

            for obj in opening_hour_formset.deleted_objects:
                obj.delete()
            messages.success(request, 'Opening hours updated successfully')
            return redirect('dashboard:update-branch', pk=branch_id)
        else:
            # If formset is invalid, display the formset with errors
            print(opening_hour_formset.errors)
            messages.error(
                request, 'Please correct the days or time errors below.')
            return render(request, 'branch/update-opening-hours.html', {
                'branch': branch,
                'opening_hour_formset': opening_hour_formset,
            })


class ViewDeleteBranchView(View):
    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
        messages.success(request, 'Branch deleted sucessfully')
        return redirect('dashboard:view-admin-branch')
