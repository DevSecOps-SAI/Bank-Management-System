from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit']

widgets = {
    'patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name'}),
    'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
}
