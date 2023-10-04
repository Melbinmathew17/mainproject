from django.db import models

# Create your models here.
class appoinmentdb(models.Model):
    department=models.CharField(max_length=100,null=True,blank=True)
    doctor=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.CharField(null=True,blank=True,max_length=100)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)



class userlogin(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)

class messagedb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
