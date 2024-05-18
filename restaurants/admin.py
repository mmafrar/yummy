from django.contrib import admin
from .models import Branch, Day

# Register your models here.


# admin.site.register(Day)


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_address',
                    'branch_contact', 'opening_time', 'closing_time')


admin.site.register(Branch, BranchAdmin)
