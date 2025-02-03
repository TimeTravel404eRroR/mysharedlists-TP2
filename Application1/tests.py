from django.test import TestCase

from .models import Item, Store
# Create your tests here.

class StoreItemTest(TestCase):

    @classmethod
    def setUpClass(cls):
        print('trigger setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('trigger tearDownClass')
    
    def setUp(self):
        print('trigger setUp')
    
    def test_create_store(self):
        self.assertFalse(False)

    def test_create_item(self):
        self.assertTrue(True)