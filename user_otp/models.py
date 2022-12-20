from django.db import models
import random
# Create your models here.
class CustomerUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name