from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'rm', 'id': 'menuPrice'})
    )

    class Meta:
        model = Menu
        fields = ['name', 'description', 'image', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu name', 'id': 'menuName'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter menu description', 'id': 'menuDescription'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'menuImage'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'menuCategory'}),
        }
