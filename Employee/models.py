from django.db import models

class Employee(models.Model):
    
    Eid = models.CharField(max_length = 10)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    PhoneNo = models.CharField(max_length = 20, null = False)
    Role = models.CharField(max_length = 50)
    Salary = models.CharField(max_length = 10, null = False)
    PF = models.CharField(max_length = 10, null = False)

    
