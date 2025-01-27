from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }
