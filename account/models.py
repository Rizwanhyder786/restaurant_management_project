from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auyh.models import User
#User profile to extend built-in User model
class UserProfile(models.model):
    user = models.OneToOneField(user,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,blank=True)
    address + models.TextField(blank=True)
    date_of_brith = models.DataField(null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username