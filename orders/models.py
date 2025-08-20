from django.db import models

# Create your models here.
class Order(models.model):
    customer_name =models.Charfield(max_length=100)
    product_name=models.Charfield(max_length=100)
    quantity=models.PostiveIntegerField()
    price=models.DeciamlField(max_digits=10),decimal_places=2)
    created_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.custumer_name}-{self.product_name}"
