from django import forms
from django.contrib.auth.models import User
from . import models

class DonorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model = models.Donor
        fields = ['bloodgroup', 'address', 'mobile', 'profile_pic']
        widgets = {
            'bloodgroup': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = models.BloodDonate
        fields = ['age', 'bloodgroup', 'disease', 'unit']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bloodgroup': forms.TextInput(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.NumberInput(attrs={'class': 'form-control'}),
        }
