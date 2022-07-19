from django import forms
from .models import Applicants

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Applicants
#         fields = "__all__"

class NameForm(forms.ModelForm):
        model = Applicants
        
        feilds = ('BIB', 'chipcode1', 'chipcode2')

        widgets = {
            'BIB': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BIB'}),
            'chipcode1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'chipcode1'}),
            'chipcode2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'chipcode2'}),
        }