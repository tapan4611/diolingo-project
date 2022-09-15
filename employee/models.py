from django.db import models

# Create your models here.
from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  

class Catagory(models.Model):  
    cid = models.CharField(max_length=20)
    cname = models.CharField(max_length=20)
    cdescription = models.CharField(max_length=50)  
    class Data:
          class Catagory(models.Model):
            db_table = "Catagory"  
