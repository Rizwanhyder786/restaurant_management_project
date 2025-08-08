from django.db import models

# Create your models here.
class item(models.model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description= models.TextField(blank=True)
    is_available=models.BooleanField(default=True)
    created_at = models.DateTimeFeild(auto_now_add=True)
    def __str__(self):
        return self.name
