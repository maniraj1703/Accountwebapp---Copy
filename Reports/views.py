from django.shortcuts import render
from Purchase.models import Bills

from Expenses.models import Expenses
from Expenses.forms import ExpensesForm
from Banking.models import Withdraw,Credit_Amount
from Sales.models import SalesBill
from Sales.forms import SalesOrderForm


# Create your views here.


def bills_view(request):
    bills = Bills.objects.all()
    return render(request,'Report/bills.html', {'bills': bills})


def expense_view(request):
    expense =Expenses.objects.all()
    return render (request,'Report/exp.html',{'expenses':expense})


def bank_view(request):
    cre = Credit_Amount.objects.all()
    deb = Withdraw.objects.all()
    return render (request,'Report/bank.html',{'credit':cre,'withdraw':deb})   


def sale_view(request):
    sales = SalesBill.objects.all()
    return render (request,'Report/sale.html',{'bills':sales})    


