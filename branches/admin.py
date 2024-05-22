from django.contrib import admin
from .models import Branch, OpeningHour


class OpeningHourInline(admin.TabularInline):
    model = OpeningHour
    extra = 1


class BranchAdmin(admin.ModelAdmin):
    inlines = [OpeningHourInline]


admin.site.register(Branch, BranchAdmin)
