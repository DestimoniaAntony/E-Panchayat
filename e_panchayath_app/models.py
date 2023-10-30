from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)
       
class Citizen(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    gender=models.CharField( max_length=10,null=True)
    marital_status=models.CharField( max_length=10,null=True)
    birth_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    address_line1=models.CharField(max_length=20,null=True)
    address_line2=models.CharField(max_length=20,null=True)
    pincode=models.CharField(max_length=6,null=True)
    ward=models.IntegerField(null=True)
    panchayat=models.CharField(max_length=25,null=True)
    password=models.CharField(max_length=10,null=True)
    
class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    gender=models.CharField( max_length=10,null=True)
    marital_status=models.CharField( max_length=10,null=True)
    birth_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    qualification=models.CharField(max_length=20,null=True)
    address_line1=models.CharField(max_length=20,null=True)
    address_line2=models.CharField(max_length=20,null=True)
    pincode=models.CharField(max_length=6,null=True)
    password=models.CharField(max_length=10,null=True)
    
class Service(models.Model):
    service = models.CharField(max_length=20,null=True)
    
class Request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    
class Application(models.Model):
    user = models.ForeignKey(Citizen,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/', null=True)
    mobile=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=20,null=True)
    gender=models.CharField( max_length=10,null=True)
    marital_status=models.CharField( max_length=10,null=True)
    birth_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    address_line1=models.CharField(max_length=20,null=True)
    address_line2=models.CharField(max_length=20,null=True)
    country=models.CharField(max_length=25,null=True)
    state=models.CharField(max_length=25,null=True)
    district=models.CharField(max_length=25,null=True)
    pincode=models.CharField(max_length=6,null=True)
    ward=models.IntegerField(null=True)
    panchayat=models.CharField(max_length=25,null=True)
    password=models.CharField(max_length=10,null=True)
    status = models.CharField(max_length=50, null=True)
    
class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='media/', null=True)
    desc=models.TextField(null=True)
    price=models.IntegerField(null=True)