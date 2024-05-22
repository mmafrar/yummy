from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Branch


class ViewBranchesView(View):

    def get(self, request):
        all_branches = Branch.objects.prefetch_related('opening_hours').all()
        context = {'all_branches': all_branches}
        return render(request, "branches.html", context)
