from django.db import models
from django.utils import timezone
from email.policy import default
from datetime import datetime, date

class Banking(models.Model):
    Bank_Name = models.CharField(max_length = 30)
    IFSC_Number = models.CharField(max_length = 10)
    Account_Number = models.IntegerField()
    Holder_Name = models.CharField(max_length = 25)
    Mobile_Number = models.IntegerField()
    Balance = models.IntegerField()
    class Meta:
        db_table="Banking"

class Vendor(models.Model):
    Bank_Name = models.CharField(max_length = 30)
    IFSC_Number = models.CharField(max_length = 10)
    Account_Number = models.IntegerField()
    Holder_Name = models.CharField(max_length = 25)
    Mobile_Number = models.IntegerField()
    class Meta:
        db_table = 'Vendor'

class Customer(models.Model):
    Bank_Name = models.CharField(max_length = 30)
    IFSC_Number = models.CharField(max_length = 10)
    Account_Number = models.IntegerField()
    Holder_Name = models.CharField(max_length = 25)
    Mobile_Number = models.IntegerField()
    class Meta:
        db_table = 'Customer'

class Amount(models.Model):
    Account_Number =  models.IntegerField()
    IFSC_Number = models.CharField(max_length = 10)
    Holder_Name = models.CharField(max_length = 25) 
    Money = models.IntegerField()
    Note = models.CharField(max_length = 50)

    class Meta:
        db_table = "Amount"

class Withdraw(models.Model):
    S_No = models.IntegerField(primary_key=True)
    Current_Balance = models.IntegerField()
    Acc_Num = models.IntegerField()
    Debit = models.IntegerField()
    Date = models.DateField(default = datetime.now())
    
    class Meta:
        db_table ="Withdraw"

class Credit_Amount(models.Model):
    S_No = models.IntegerField(primary_key=True)
    Current_Balance = models.IntegerField()
    Acc_Num = models.IntegerField()
    Credit = models.IntegerField()
    Date = models.DateField(default = datetime.now())

    class Meta:
        db_table ="Credit_Amount"
