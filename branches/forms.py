from django import forms
from django.forms.models import modelformset_factory

from .models import Branch, OpeningHour


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name', 'branch_address',
                  'branch_contact', 'branch_image']
        widgets = {
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name'}),
            'branch_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch address'}),
            'branch_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch contact'}),
            'branch_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = OpeningHour
        exclude = ['id']
        fields = ['day', 'open_time', 'close_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-select'}),
            'open_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'close_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


OpeningHourFormSet = modelformset_factory(
    OpeningHour,
    fields=('day', 'open_time', 'close_time'),
    extra=1,  # Number of extra empty forms to display
    can_delete=True
)
