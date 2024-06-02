import os
import json
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Sum, Count
from django.db.models.functions import TruncWeek
from django.shortcuts import render, redirect, get_object_or_404

from .models import Menu
from .forms import MenuForm
from orders.models import Order, OrderStatus
from branches.models import Branch, OpeningHour
from branches.forms import BranchForm, OpeningHourFormSet


class DashboardAdminView(View):

    def get(self, request):
        total_orders = Order.objects.count()

        total_accepted = Order.objects.filter(
            order_status=OrderStatus.ACCEPTED).count()

        total_rejected = Order.objects.filter(
            order_status=OrderStatus.REJECTED).count()

        total_revenue = Order.objects.filter(order_status=OrderStatus.ACCEPTED).aggregate(
            total_revenue=Sum('total_amount'))['total_revenue']

        popular_menu_names = []
        popular_menus = Order.objects.values('menu_id').annotate(
            count=Count('menu_id')).order_by('-count')[:3]

        for popular_menu in popular_menus:
            popular_menu_names.append(Menu.objects.get(
                id=popular_menu['menu_id']).name)

        # Aggregate monthly revenue data
        weekly_revenue = Order.objects.filter(order_status=OrderStatus.ACCEPTED).annotate(week=TruncWeek(
            'created_at')).values('week').annotate(total_revenue=Sum('total_amount')).order_by('week')

        # Prepare data for Chart.js
        weeks = [entry['week'].strftime('%Y-%m-%d')
                 for entry in weekly_revenue]
        revenues = [entry['total_revenue'] for entry in weekly_revenue]

        context = {
            'user': request.user,
            'total_orders': total_orders,
            'total_accepted': total_accepted,
            'total_rejected': total_rejected,
            'total_revenue': total_revenue,
            'popular_menu_names': popular_menu_names,
            'weeks': json.dumps(weeks),
            'revenues': json.dumps(revenues),
        }

        return render(request, "dashboard-admin.html", context)


class BranchAdminView(View):

    def get(self, request):
        all_branches = Branch.objects.all().order_by('-id')
        context = {'all_branches': all_branches}
        return render(request, "branches/branch-admin.html", context)


class BranchCreateView(View):
    def get(self, request):
        branch_form = BranchForm()
        opening_hour_formset = OpeningHourFormSet(
            queryset=OpeningHour.objects.none())
        return render(request, 'branches/branch-create.html', {'branch_form': branch_form, 'opening_hour_formset': opening_hour_formset})

    def post(self, request):
        branch_form = BranchForm(request.POST, request.FILES)
        opening_hour_formset = OpeningHourFormSet(request.POST)

        if branch_form.is_valid() and opening_hour_formset.is_valid():
            branch_name = branch_form.cleaned_data['branch_name']
            if Branch.objects.filter(branch_name=branch_name).exists():
                messages.error(request, 'Branch already exists.')
                return render(request, 'branches/branch-create.html', {
                    'branch_form': branch_form,
                    'opening_hour_formset': opening_hour_formset, })
            else:
                days = set()
                for form in opening_hour_formset.forms:
                    day = form.cleaned_data.get('day')
                    if day in days:
                        messages.error(
                            request, 'Duplicate day found in opening hours.')
                        return render(request, 'branches/branch-create.html', {
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
        return render(request, 'branches/branch-create.html', {
            'branch_form': branch_form,
            'opening_hour_formset': opening_hour_formset})


class BranchEditView(View):
    def get(self, request, pk):
        branch_instance = get_object_or_404(Branch, pk=pk)
        branch_form = BranchForm(instance=branch_instance)
        return render(request, 'branches/branch-edit.html', {
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

        return render(request, 'branches/branch-edit.html', {
            'branch_form': branch_form,
            'branch_id': pk
        })


class BranchEditOpeningHoursView(View):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        opening_hours = OpeningHour.objects.filter(branch=branch)
        opening_hour_formset = OpeningHourFormSet(queryset=opening_hours)
        return render(request, 'branches/branch-edit-opening-hours.html', {
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

        return render(request, 'branches/branch-edit-opening-hours.html', {
            'branch': branch,
            'opening_hour_formset': opening_hour_formset,
        })


class BranchDeleteView(View):
    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        if Order.objects.filter(branch=branch).exists():
            messages.error(
                request, 'Cannot delete branch as there are orders associated with it.')
            return redirect('dashboard:branches.index')
        else:
            branch.delete()
            messages.success(request, 'Branch deleted successfully')
            return redirect('dashboard:branches.index')


class MenuAdminView(View):

    def get(self, request):
        menus = Menu.objects.all()
        return render(request, "menus/menu-admin.html", {'menus': menus})


class MenuCreateView(View):

    def get(self, request):
        form = MenuForm()
        return render(request, "menus/menu-create.html", {'form': form})

    def post(self, request):
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu added successfully')
            return redirect('dashboard:menus.index')
        else:
            return render(request, "menus/menu-create.html", {'form': form})


class MenuEditView(View):

    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        form = MenuForm(instance=menu)
        return render(request, "menus/menu-edit.html", {'form': form, 'menu': menu})

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
            return render(request, "menus/menu-edit.html", {'form': form, 'menu': menu, 'errors': errors})


class MenuDeleteView(View):

    def get(self, request, pk):

        menu = get_object_or_404(Menu, pk=pk)
        image_path = menu.image.path

        if Order.objects.filter(menu=menu).exists():
            messages.error(
                request, 'Cannot delete menu as there are orders associated with it.')
            return redirect('dashboard:menus.index')

        if os.path.exists(image_path):
            os.remove(image_path)
            menu.delete()
            messages.success(request, 'Menu deleted successfully')
        return redirect('dashboard:menus.index')


class OrderAdminView(View):

    def get(self, request):
        all_orders = Order.objects.all()
        return render(request, "orders/order-admin.html", {'all_orders': all_orders})


class OrderDetailView(View):

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_status = request.GET.get('order_status')
        if order_status is not None:
            order.order_status = order_status
            order.save()
            messages.success(request, 'Order status updated successfully')
        return render(request, "orders/order-detail.html", {'order': order})
