from django.test import TestCase
from .models import item

# Create your tests here.
class itemModelTest(TestCase):
    def setUp(self):
        item.objects.create(name='burger',price=999.93)
    def test_item_name(self):
        item = item.objects.get(name"burger)
        self.assertEqual(item.name,"burger")