from django.db import models
from donor.models import Donor
from patient.models import Patient

class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=500)
    status = models.CharField(default='Pending', max_length=20)

    request_by_donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True)
    request_by_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    
    date = models.DateField(auto_now=True)


        