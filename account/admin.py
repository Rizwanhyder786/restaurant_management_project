from django.contrib import admin

# Register your models here.
'''The restaurant_management,with a sub-folder structure that includes:
.products/
.orders/
Each of these has the usual django files:
.admin.py
.apps.py
.models.py
.tests.py
.views.py'''

from django.db import models
class products(models.model):
    name=models.charfield(max_lenght=100)
    price=models.DecimalField(max_digits=10),
decimal_places=2)

from django.contrib import admin
from .models import products
admin.site.register(products)

