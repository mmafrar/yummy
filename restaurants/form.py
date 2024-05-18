from django import forms
from .models import Branch


class AddBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('branch_name', 'branch_address', 'branch_contact',
                  'branch_image', 'day', 'opening_time', 'closing_time')
        widgets = {
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name'}),
            'branch_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch address'}),
            'branch_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch contact'}),
            'branch_image': forms.FileInput(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
        }
