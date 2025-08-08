from django.contrib import admin
from .models import Order #import your order model

# Register your models here.
class OrderAdmin(admin.modeladmin):
    list_display = ('id','customer_name','item_name','quantity','created_at')
    search_fields =('customer_name','item_name')
    list_filter = ('created_at',)
# register the model with custom admin
admin.site.register(order,orderAdmin)