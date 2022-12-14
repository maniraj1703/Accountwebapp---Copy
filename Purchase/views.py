from django.shortcuts import render, redirect
from Purchase.models import Bills,Vendor,Vendororder

from Purchase import views
from django.http import HttpResponse
from sqlite3 import *




#  --------------------------for Bills-----------------------------




def bills_register(request):
    if request.method == 'POST':
         Vendor_Id = request.POST['Vendor_Id']
         VendorName = request.POST['VendorName']
         VendorPhoneNo = request.POST['VendorPhoneNo']
         Product = request.POST['Product']
         ProductQuantity  = request.POST['ProductQuantity']
         Price = request.POST['Price']
         Total_Price  = request.POST['Total_Price']
         RecivedDate = request.POST['RecivedDate']
         obj=Bills()
         obj.Vendor_Id = Vendor_Id
         obj.VendorName = VendorName
         obj.VendorPhoneNo = VendorPhoneNo
         obj.Product = Product
         obj.ProductQuantity  = ProductQuantity 
         obj.Price = Price
         obj.Total_Price = Total_Price
         obj.RecivedDate = RecivedDate
         obj.save()
         return redirect('bills')
    return render(request,'Purchase/add_bills.html')



    
    

def bills_view(request):
    bills = Bills.objects.all()
    if (bills!=''):
        return render(request,'Purchase/bills.html', {'bills': bills})
    else:
        return render (request,'Purchase/bills.html',)

def delete_bills(request, pk):
    bills = Bills.objects.get(id = pk)
    bills.delete()
    return redirect('bills')




def update_bills(request, pk):
        bills = Bills.objects.get(id = pk)
        if request.method == 'POST':
         Product = request.POST['Product']
         ProductQuantity  = request.POST['ProductQuantity']
         Price = request.POST['Price']
         Total_Price  = request.POST['Total_Price']
         bills.Product = Product
         bills.ProductQuantity  = ProductQuantity 
         bills.Price = Price
         bills.Total_Price = Total_Price
         bills.save()
         return redirect('bills')
        return render(request,'Purchase/update_bills.html',{'bills':bills})


  
def search_bills_view(request):
    
    bills = ""
    
    if request.GET.get("query"):
        bills = Bills.objects.filter(Product = request.GET.get("query"))
        print(bills)
    return render(request,'Purchase/bills.html',{'bills': bills})


#<------- for Orders ------------------------------------------------------------------------------------------------------->

def orders_register(request):
    ven = Vendororder.objects.all()    
    if request.method == "POST":
        VendorName=request.POST['VendorName']
        Phone_No=request.POST['Phone_No']
        Product=request.POST['Product']
        ProductQuantity=request.POST['ProductQuantity']
        Price=request.POST['Price']
        TotalPrice=request.POST['TotalPrice']
        Ordereddate=request.POST['Ordereddate']
        ven=Vendororder()
        ven.VendorName=VendorName
        ven.Phone_No=Phone_No
        ven.Product=Product
        ven.Product_Quantity=ProductQuantity
        ven.Price=Price
        ven.Total_Price=TotalPrice
        ven.Ordereddate=Ordereddate
        ven.save()


    #ordDict = {
    #ordDict = {
    #ordDict = {
     #   'ordForm': OrdersForm()
    #}
    #if request.method == 'POST':
     #   ordForm = OrdersForm(request.POST)
      #  if ordForm.is_valid():
       #     ordForm.save(commit=True)
            
        #pass
    #return render(request, 'Purchase/add_order.html', context = ordDict)
    ve= Vendor.objects.all()
    if (ve!=''):

        return render (request,'Purchase/select_vendor.html',{'vend':ve})
    else:
         return render (request,'Purchase/select_vendor.html')

def orders_reg(request,pk):
    ven = Vendor.objects.get(id=pk)
    vendorForm = VendorForm(instance = ven)
    vendDict = {
       'vendForm': vendorForm()
    }
    if request.method == 'POST':
        vendorForm = VendorForm(request.POST)
        if vendorForm.is_valid():
            vendorForm.save(commit=True)
            
        pass
    return render(request, 'Purchase/add_order.html', context = vendDict)

 
   

def orders_view(request):
    order = Vendororder.objects.all().filter()
    return render(request,'Purchase/order.html', {'orders': order})

def select_vendor(request):
    vendor = Vendor.objects.all()
    return render(request,'Purchase/select_vendor.html',{'vendor': vendor})


    
 
def delete_orders(request, pk):
    orders = Vendororder.objects.get(id = pk)
    orders.delete()
    return orders_view(request)

def update_orders(request, pk):
    orders = Vendororder.objects.get(id = pk)
    if request.method=='POST':
       
        Product = request.POST['Product']
        Product_Quantity = request.POST['Product_Quantity']
        Price = request.POST['Price']
        Total_Price = request.POST['Total_Price']
     
       
        orders.Product=  Product
        orders.Product_Quantity = Product_Quantity
        orders.Price = Price
        orders. Total_Price =  Total_Price
   
        orders.save()
        return redirect('orders')
    return render(request, 'Purchase/update_order.html',{'Vendororder':orders})

    ordersForm = venForm(instance = orders)

    orders_dict = {
        'ordersForm': ordersForm
    }

    if request.method=='POST':
        ordersForm = venForm(request.POST, instance = orders)

        if ordersForm.is_valid():
            orders = ordersForm.save(commit=True)
            orders.save()
    return render(request, 'Purchase/update_order.html', context = orders_dict)

def search_order_view(request):
    
    orders = ""
    
    if request.GET.get("query"):
        orders = Vendororder.objects.filter(Product = request.GET.get("query"))
        print(orders)
    return render(request,'Purchase/order.html',{'orders': orders})







    #<--------------------------Vendor ---------------------------------->
def vendor_register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Phone_No = request.POST['Phone_No']
        Email = request.POST['Email']
        Billing_Address = request.POST['Billing_Address']
        obj=Vendor()
        obj.Name = Name
        obj.Phone_No = Phone_No
        obj.Email = Email
        obj.Billing_Address = Billing_Address
        obj.save()
      
    return render(request,'Purchase/add_vendor.html')



def vendor_display(request):
        vendor = Vendor.objects.all()
        
        return render(request,'Purchase/select_vendor.html',context=vendor)



    

def vendor_view(request):
    vendor = Vendor.objects.all()
    if(vendor!=''):
        return render(request,'Purchase/vendor.html', {'vendor': vendor})
    else:
        return render(request,'Purchase/vendor.html')


def delete_vendor(request,pk):
    vendor = Vendor.objects.get(id = pk)
    vendor.delete()
    return vendor_view(request)

def update_vendor(request,pk):
    vendor = Vendor.objects.get(id = pk)
    if request.method == 'POST':
        Name = request.POST['Name']
        Phone_No = request.POST['Phone_No']
        Email = request.POST['Email']
        Billing_Address = request.POST['Billing_Address']
        vendor.Name = Name
        vendor.Phone_No = Phone_No
        vendor.Email = Email
        vendor.Billing_Address = Billing_Address
        vendor.save()
        return redirect('pur_ven')
    return render(request, 'Purchase/update_vendor.html', {'vendor':vendor})

        
      
     



def search_vendor_view(request):
    vendor = ""
    if request.GET.get("query"):
        vendor = Vendor.objects.filter(Name = request.GET.get("query"))
        print(vendor)
    return render(request,'Purchase/vendor.html',{'vendor': vendor})

    

