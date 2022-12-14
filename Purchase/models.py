from datetime import datetime
from django.db import models
from email.policy import default


class Bills(models.Model):

    Vendor_Id = models.IntegerField()
    VendorName = models.CharField(max_length = 50)
    VendorPhoneNo = models.IntegerField()
    Product = models.CharField(max_length = 50)
    ProductQuantity = models.IntegerField()
    Price = models.IntegerField()
    Total_Price = models.IntegerField()
    RecivedDate = models.DateTimeField()
    def __str__(self):
        return self.VendorName


class Orders(models.Model):

    Vendor_Id = models.IntegerField()
    VendorName = models.CharField(max_length=50)
    VendorPhoneNo = models.IntegerField()
    Product = models.CharField(max_length = 50)
    ProductQuantity = models.IntegerField()
    Price = models.IntegerField()
    Total_Price = models.IntegerField()
    OrderedDate = models.DateField(default = datetime.now())
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.Product + ' has ' + str(self.ProductQuantity) + ' is ' + str(self.Price) + 'rs'


class Vendor(models.Model):
    
    Name = models.CharField(max_length = 50)
    Phone_No = models.CharField(max_length = 10, null = False)
    Email = models.EmailField(max_length = 50)
    Billing_Address = models.CharField(max_length = 100)
    def __str__ (self):
        return self.Name  

class Vendororder(models.Model):
    
    VendorName = models.CharField(max_length=100)
    Phone_No = models.IntegerField()
    Product = models.CharField(max_length=150)
    Product_Quantity = models.IntegerField()
    Price = models.IntegerField()
    Total_Price = models.IntegerField()
    Ordereddate = models.DateField(default = datetime.now())
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    # return self.Product + ' has ' + str(self.Product_Quantity) + ' is ' + str(self.Price) + 'rs'   
	    return self.Product
    

      

    
