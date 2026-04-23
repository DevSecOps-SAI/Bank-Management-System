from django import forms
from django.contrib.auth.models import User
from . import models

class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['age', 'bloodgroup', 'disease', 'address', 'doctorname', 'mobile', 'profile_pic']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bloodgroup': forms.TextInput(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'doctorname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
        }