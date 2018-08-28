from django.test import TestCase
from .models import Product

class ProductTest(TestCase):

    def test_str(self):
        test_name = Product(name="A Product")
        self.assertEqual(str(test_name), "A Product")

