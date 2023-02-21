from django.db import models

# Create your models here.
class Donations(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,default='0')
    designation = models.CharField(max_length=100,default='-')
    donations = models.CharField(max_length=10000000,default='{"to":[],"status":"In Progress","email":[],"phone":[],"date":[]}')
    def __str__(self) -> str:
        return self.name