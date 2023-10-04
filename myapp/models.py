from django.db import models

# Create your models here.
class departmentdb(models.Model):
    Department=models.CharField(max_length=100,null=True,blank=True)
    Describe=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Profile")

class doctorsdb(models.Model):
    Departmentname=models.CharField(max_length=100,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Qualification=models.CharField(max_length=100,null=True,blank=True)
    About=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to="Doctorimage")


class service_db(models.Model):
    Service = models.CharField(max_length=100, null=True, blank=True)
    Describe = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="ServiceProfile")