from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
import os

from .models import Menu
from .forms import MenuForm
from orders.models import Order
from branches.models import Branch, OpeningHour
from branches.form import BranchForm, OpeningHourFormSet


class ViewDashboardView(View):

    def get(self, request):
        return render(request, "dashboard/index.html")


class ViewAdminBranchs(View):

    def get(self, request):
        all_branches = Branch.objects.all().order_by('-id')
        context = {'all_branches': all_branches}
        return render(request, "branches/admin-branch.html", context)


class ViewAddBranchView(View):
    def get(self, request):
        branch_form = BranchForm()
        opening_hour_formset = OpeningHourFormSet(
            queryset=OpeningHour.objects.none())
        return render(request, 'branches/add-branch.html', {'branch_form': branch_form, 'opening_hour_formset': opening_hour_formset})

    def post(self, request):
        branch_form = BranchForm(request.POST, request.FILES)
        opening_hour_formset = OpeningHourFormSet(request.POST)

        if branch_form.is_valid() and opening_hour_formset.is_valid():
            branch_name = branch_form.cleaned_data['branch_name']
            if Branch.objects.filter(branch_name=branch_name).exists():
                messages.error(request, 'Branch already exists.')
                return render(request, 'branches/add-branch.html', {
                    'branch_form': branch_form,
                    'opening_hour_formset': opening_hour_formset, })
            else:
                days = set()
                for form in opening_hour_formset.forms:
                    day = form.cleaned_data.get('day')
                    if day in days:
                        messages.error(
                            request, 'Duplicate day found in opening hours.')
                        return render(request, 'branches/add-branch.html', {
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
                return redirect('dashboard:branches.index')
        return render(request, 'branches/add-branch.html', {
            'branch_form': branch_form,
            'opening_hour_formset': opening_hour_formset})


class ViewUpdateBranchView(View):
    def get(self, request, pk):
        branch_instance = get_object_or_404(Branch, pk=pk)
        branch_form = BranchForm(instance=branch_instance)
        return render(request, 'branches/update-branch.html', {
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
                return redirect('dashboard:branches.index')

        return render(request, 'branches/update-branch.html', {
            'branch_form': branch_form,
            'branch_id': pk
        })


class ViewUpdateOpeningHoursView(View):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        opening_hours = OpeningHour.objects.filter(branch=branch)
        opening_hour_formset = OpeningHourFormSet(queryset=opening_hours)
        return render(request, 'branches/update-opening-hours.html', {
            'branch': branch,
            'opening_hour_formset': opening_hour_formset,
        })

    def post(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        opening_hours = OpeningHour.objects.filter(branch=branch)
        opening_hour_formset = OpeningHourFormSet(
            request.POST, queryset=opening_hours)

        if opening_hour_formset.is_valid():
            try:
                # Save the formset if it's valid
                opening_hour_instances = opening_hour_formset.save(
                    commit=False)
                for opening_hour_instance in opening_hour_instances:
                    opening_hour_instance.branch = branch  # Set the branch before saving
                    opening_hour_instance.save()

                for obj in opening_hour_formset.deleted_objects:
                    obj.delete()

                messages.success(request, 'Opening hours updated successfully')
                return redirect('dashboard:branches.edit', pk=branch_id)
            except IntegrityError as e:
                # Handle the integrity error for duplicate days
                messages.error(
                    request, 'A duplicate entry exists for the same day.')
        else:
            # If formset is invalid, display the formset with errors
            print(opening_hour_formset.errors)
            messages.error(request, 'Please correct the errors below.')

        return render(request, 'branch/update-opening-hours.html', {
            'branch': branch,
            'opening_hour_formset': opening_hour_formset,
        })


class ViewDeleteBranchView(View):
    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
        messages.success(request, 'Branch deleted sucessfully')
        return redirect('dashboard:branches.index')


class ViewAdminMenu(View):

    def get(self, request):
        menus = Menu.objects.all()
        return render(request, "menus/admin-menu.html", {'menus': menus})


class AddMenuView(View):

    def get(self, request):
        form = MenuForm()
        return render(request, "menus/add-menu.html", {'form': form})

    def post(self, request):
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu added successfully')
            return redirect('dashboard:menus.index')
        else:
            return render(request, "menus/add-menu.html", {'form': form})


class ViewUpdateMenuView(View):

    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        form = MenuForm(instance=menu)
        return render(request, "menus/update-menu.html", {'form': form, 'menu': menu})

    def post(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        form = MenuForm(request.POST, request.FILES, instance=menu)

        if form.is_valid():

            old_image = Menu.objects.get(id=pk)
            image_path = old_image.image.path

            if 'image' in request.FILES:
                if os.path.exists(image_path):
                    os.remove(image_path)
            form.save()
            messages.success(request, 'Menu updated successfully')
            return redirect('dashboard:menus.index')
        else:
            errors = form.errors
            return render(request, "menus/update-menu.html", {'form': form, 'menu': menu, 'errors': errors})


class DeleteMenuView(View):

    def get(self, request, pk):

        menu = get_object_or_404(Menu, pk=pk)
        image_path = menu.image.path

        if os.path.exists(image_path):
            os.remove(image_path)
            menu.delete()
            messages.success(request, 'Menu Deleted')
        return redirect('dashboard:menus.index')


class OrderListView(View):

    def get(self, request):
        all_orders = Order.objects.all()
        args = {'all_orders': all_orders}
        return render(request, "orders/order-list.html", args)


class OrderDetailView(View):

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_status = request.GET.get('order_status')
        if order_status is not None:
            order.order_status = order_status
            order.save()
        args = {'order': order}
        return render(request, "orders/order-detail.html", args)
