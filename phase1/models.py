from django.db import models



class UserDetail(models.Model):
    name=models.CharField(unique=True, max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=50)

    def __str__(self): 
        return self.name 
    
class Advocates(models.Model):
    name=models.CharField(unique=True, max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, null=True)
    enrollment_id=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=50,default='password123')
    address=models.CharField(max_length=255, null=True)
    active=models.BooleanField(default=False)
    fee_paid = models.BooleanField(default=False)
    website=models.BooleanField(default=False)
    id_image = models.ImageField(upload_to='imagestore/', null=True, blank=True)
    def __str__(self): 
        return self.name