from email.policy import default
from enum import auto
from django.db import models
from django.utils import timezone
from Purchase.models import Vendororder


class CustomerDetails(models.Model):
    
    type = [('Individual Person','Individual Person'),
    ('Buissness Person','Buissness Person')]
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    PhoneNo = models.CharField(max_length = 20, null = False)
    CustomerType = models.CharField(max_length = 70, choices = type)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class SalesBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(CustomerDetails, on_delete = models.CASCADE, related_name='salescustomer')

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return SalesItem.objects.filter(billno=self)

    def get_total_price(self):
        purchaseitems = SalesItem.objects.filter(billno=self)
        total = 0
        for item in purchaseitems:
            total += item.totalprice
        return total

class SalesItem(models.Model):
    billno = models.ForeignKey(SalesBill, on_delete = models.CASCADE, related_name='salesbillno')
    stock = models.ForeignKey(Vendororder, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.Product

class SalesBillDetails(models.Model):
    billno = models.ForeignKey(SalesBill, on_delete = models.CASCADE, related_name='salesdetailsbillno')
    
    eway = models.CharField(max_length=50, blank=True, null=True)    
    veh = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)

class SalesOrder(models.Model):

    
    CustomerName = models.CharField(max_length = 50)
    CustomerPhoneNo = models.CharField(max_length = 20, null = False)
    Product = models.CharField(max_length = 50)
    ProductQuantity = models.IntegerField()
    Price = models.CharField(max_length = 20)
    OrderedDate = models.DateTimeField(default = timezone.now())
    supplier = models.ForeignKey(CustomerDetails, on_delete = models.CASCADE, related_name='purchasesupplier')


    

    


     


 

