from django.test import TestCase
from django.contrib.auth.models import User
from .models import Donor, BloodDonate

class DonorModelTest(TestCase):
    def test_create_donor(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        donor = Donor.objects.create(user=user, bloodgroup='A+', mobile='1234567890', address='City')
        self.assertEqual(donor.user.username, 'testuser')
        self.assertEqual(donor.bloodgroup, 'A+')
