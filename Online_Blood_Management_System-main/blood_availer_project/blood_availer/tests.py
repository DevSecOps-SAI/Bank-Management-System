from django.test import TestCase
from .models import Stock

class StockModelTest(TestCase):
    def test_stock_creation(self):
        stock = Stock.objects.create(bloodgroup="A+", unit=5)
        self.assertEqual(stock.bloodgroup, "A+")
        self.assertEqual(stock.unit, 5)
