from django.urls import path
from .views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('order/',include('orders.urls')),#includes order app urls
]