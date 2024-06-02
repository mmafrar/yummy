from django.views import View
from django.shortcuts import render

from .models import Branch


class BranchIndexView(View):

    def get(self, request):
        all_branches = Branch.objects.prefetch_related('opening_hours').all()
        context = {'all_branches': all_branches}
        return render(request, "branch-index.html", context)
