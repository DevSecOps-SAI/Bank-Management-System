
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Patient

class PatientModelTest(TestCase):
    def test_create_patient(self):
        user = User.objects.create_user(username='patientuser', password='testpass')
        patient = Patient.objects.create(
            user=user,
            age=30,
            bloodgroup='O+',
            disease='None',
            address='City',
            doctorname='Dr. Smith',
            mobile='9999999999'
        )
        self.assertEqual(patient.user.username, 'patientuser')
        self.assertEqual(patient.bloodgroup, 'O+')