from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    location = models.TextField(max_length=122)
    about = models.CharField(max_length=122)
    type = models.CharField(max_length=20, choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phone','Mobile Phone')))
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name +' -- '+ self.location

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager','Manager'),('Software Developer','sd'),('Project Leader','pl')))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)