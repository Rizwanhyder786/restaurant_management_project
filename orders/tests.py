from django.test import TestCase
from .models import Order

# Create your tests here.

class OrderModelTest(TestCase):
    def setup(self):
        #create a sample order before each test
        Order.objects.create(
            customer_name="Rizwan",
            product_name="Laptop",
            qunanity=2,
            price=50000.00
        )
    def test_order_created(self):
        '''check if the order is saved correctly'''
        order=order.objects.get(customer_name="Rizwan")
        self.assertEqual(order.product_name, "Laptop")
        self.assertEqual(orderquantity,2)
        self.assertEqual(float(order.price),50000.00)
    def test_str_method(self):
        '''check if __str__ return correct format'''
        order =order.objects.get(customer_name="Rizwan")
        self.assertEqual(str(order),"Rizwan - Laptop")