from django.shortcuts import render, redirect
from Banking.models import Banking, Amount, Vendor, Customer, Withdraw, Credit_Amount
from sqlite3 import *

# All Bank Account views
def bank_view(request):
    bank = Banking.objects.all()
    if(bank!=''):
        return render(request,'Banking/bank.html',{'banking':bank})
    else:
        return render(request,'Banking/bank.html')

def vend_view(request):
    vend = Vendor.objects.all()
    if(vend!=''):
        return render(request,'Banking/vendor_acc.html',{'vendor':vend})
    else:
        return render(request,'Banking/vendor_acc.html')

def cus_view(request):
    cus = Customer.objects.all()
    if(cus!=''):
        return render(request,'Banking/customer_acc.html',{'customer':cus})
    else:
        return render(request,'Banking/customer_acc.html')

def withdraw_view(request):
    if request.method=='POST':
        start_date = request.POST.get('Start_Date')
        end_date = request.POST.get('End_Date')
        result = Credit_Amount.objects.raw('select S_No, Credit_Amount.Date, Credit_Amount.Current_Balance, Credit_Amount.Acc_Num, Credit_Amount.Credit from Credit_Amount where Credit_Amount.Date between "'+start_date+'" and "'+end_date+'"')
        result2 = Withdraw.objects.raw('select S_No, Withdraw.Date, Withdraw.Current_Balance, Withdraw.Acc_Num, Withdraw.Debit from Withdraw where Withdraw.Date between "'+start_date+'" and "'+end_date+'"')
        return render(request,'Banking/Transaction_History.html',{'credit':result, 'withdraw':result2})
    else:
        cre = Credit_Amount.objects.all()
        deb = Withdraw.objects.all()
        return render(request,'Banking/Transaction_History.html')

# All Bank Register
def bank_register(request):
    if request.method == 'POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']
        Balance = request.POST['Balance']
        obj=Banking()
        obj.Bank_Name = Bank_Name
        obj.IFSC_Number = IFSC_Number
        obj.Account_Number = Account_Number
        obj.Holder_Name = Holder_Name
        obj.Mobile_Number = Mobile_Number
        obj.Balance = Balance
        obj.save()
        return redirect('bank')
    return render(request,'Banking/add_bank.html')

def vendor_register(request):
    if request.method == 'POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']

        obj=Vendor()
        obj.Bank_Name = Bank_Name
        obj.IFSC_Number = IFSC_Number
        obj.Account_Number = Account_Number
        obj.Holder_Name = Holder_Name
        obj.Mobile_Number = Mobile_Number
        obj.save()
        return redirect('vend_bank')
    return render(request,'Banking/add_vendor.html')

def customer_register(request):
    if request.method == 'POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']

        obj=Customer()
        obj.Bank_Name = Bank_Name
        obj.IFSC_Number = IFSC_Number
        obj.Account_Number = Account_Number
        obj.Holder_Name = Holder_Name
        obj.Mobile_Number = Mobile_Number
        obj.save()
        return redirect('cus_bank')
    return render(request,'Banking/add_customer.html')

# Update Bank Accounts

def update_bank(request, id):
    bank = Banking.objects.get(id = id)
    if request.method=='POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']
        Balance = request.POST['Balance']
        bank.Bank_Name = Bank_Name
        bank.IFSC_Number = IFSC_Number
        bank.Account_Number = Account_Number
        bank.Holder_Name = Holder_Name
        bank.Mobile_Number = Mobile_Number
        bank.Balance = Balance
        bank.save()
        return redirect('bank')
    return render(request, 'Banking/update_bank.html',{'banking':bank})

def update_vendor(request, id):
    vend = Vendor.objects.get(id = id)
    if request.method=='POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']
        vend.Bank_Name = Bank_Name
        vend.IFSC_Number = IFSC_Number
        vend.Account_Number = Account_Number
        vend.Holder_Name = Holder_Name
        vend.Mobile_Number = Mobile_Number
        vend.save()
        return redirect('vend_bank')
    return render(request, 'Banking/update_vendor.html',{'vendor':vend})

def update_customer(request, id):
    cus = Customer.objects.get(id = id)
    if request.method=='POST':
        Bank_Name = request.POST['Bank_Name']
        IFSC_Number = request.POST['IFSC_Number']
        Account_Number = request.POST['Account_Number']
        Holder_Name = request.POST['Holder_Name']
        Mobile_Number = request.POST['Mobile_Number']
        cus.Bank_Name = Bank_Name
        cus.IFSC_Number = IFSC_Number
        cus.Account_Number = Account_Number
        cus.Holder_Name = Holder_Name
        cus.Mobile_Number = Mobile_Number
        cus.save()
        return redirect('cus_bank')
    return render(request, 'Banking/update_customer.html',{'customer':cus})    

# Delete Bank Accounts

def delete_bank(request, id):
    bank = Banking.objects.get(id = id)
    bank.delete()
    return redirect('bank')
def delete_vendor(request, id):
    vend = Vendor.objects.get(id = id)
    vend.delete()
    return redirect('vend_bank')
def delete_customer(request, id):
    cus = Customer.objects.get(id = id)
    cus.delete()
    return redirect('cus_bank')

# Credit Amount
def add_amt(request, id):
    cre = Credit_Amount.objects.all()
    bank = Banking.objects.all()
    if request.method == 'POST':
        Current_Balance = request.POST['Balance']
        Acc_Num = request.POST['Acc_Num']
        Credit = request.POST['Credit']
        Date = request.POST['Date'] 
        cre = Credit_Amount()
        cre.Acc_Num = Acc_Num
        cre.Date = Date
        cre.Current_Balance = Current_Balance
        cre.Credit = Credit
        cre.save()        
    bank = Banking.objects.get(id = id)
    cus = Customer.objects.all()    
    if request.method=='POST':
        Balance = float(request.POST['Balance'])
        cre = float(request.POST["Credit"])
        result = Balance + cre
        bank.Balance = result
        bank.save()
        return redirect('bank')    
    if(cus!=''):
        return render(request,'Banking/add_amt.html',{'customer':cus,'banking':bank})
    else:
        return render(request,'Banking/add_amt.html')

# Debit Amount
def choose_acc(request, id):
    wit = Withdraw.objects.all()
    if request.method == 'POST':
        Current_Balance = request.POST['Current_Balance']
        Acc_Num = request.POST['Acc_Num']
        Debit = request.POST['Debit']
        Date = request.POST['Date']
        wit = Withdraw()
        wit.Acc_Num = Acc_Num
        wit.Current_Balance = Current_Balance
        wit.Debit = Debit
        wit.Date = Date
        wit.save()
    bank = Banking.objects.get(id = id)
    vend = Vendor.objects.all()
    if request.method=='POST':
        Balance = float(request.POST['Current_Balance'])
        with_d = float(request.POST["Debit"])
        result = Balance - with_d
        bank.Balance = result
        bank.save()
        return redirect('bank')
    if(vend!=''):
        return render(request,'Banking/debit_amt.html',{'vendor':vend, 'banking':bank})
    else:
        return render(request,'Banking/debit_amt.html')

# Search Accounts
def search_vendor_view(request):
    vendor = ""
    if request.GET.get("query"):
        vendor = Vendor.objects.filter(Mobile_Number = request.GET.get("query"))
        print(vendor)
    return render(request,'Banking/vendor_acc.html',{'vendor': vendor})

def search_customer_view(request):
    customer = ""
    if request.GET.get("query"):
        customer = Customer.objects.filter(Mobile_Number = request.GET.get("query"))
        print(customer)
    return render(request,'Banking/customer_acc.html',{'customer': customer})



def with_amt(request, id):
    vend = Vendor.objects.get(id = id)
    bank = Banking.objects.all()
    if request.method=='POST':
        Balance =float(request.POST['Balance'])
        with_amt = float(request.POST["with_mon"])
        result = Balance - with_amt
        bank.Balance = result
        bank.save()
        return redirect('withdraw_amt-bank')
    return render(request,'Banking/add_amt.html')
