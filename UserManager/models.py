from django.db import models

class UserManager(models.Model):

    type = [('Admin','Admin'),
    ('Accountant','Accountant')]
    
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    PhoneNo = models.CharField(max_length = 20, null = False)
    Role = models.CharField(max_length = 20, choices = type)
    Address = models.CharField(max_length = 150)
    Password = models.CharField(max_length = 20)



