from django.shortcuts import render,redirect
from Expenses.models import Expenses
from Expenses.forms import ExpensesForm




def Expenses_register(request):
    expDict = {
        'expForm': ExpensesForm()
    }
    if request.method == 'POST':
        expForm = ExpensesForm(request.POST)
        if expForm.is_valid():
            expForm.save(commit=True)
        pass
    return render(request, 'expenses/add_expense.html', context = expDict)

def expenses_view(request):
    expenses = Expenses.objects.all().filter()
    return render(request,'expenses/xpense.html', {'expenses': expenses})

def delete_expenses(request, pk):
    expenses = Expenses.objects.get(id = pk)
    expenses.delete()
    return expenses_view(request)



def search_expenses_view(request):
    expenses = ""
    if request.GET.get("query"):
        expenses = Expenses.objects.filter(Name = request.GET.get("query"))
        print(expenses)
    return render(request,'expenses/xpense.html',{'expenses': expenses})



# Create your views here.
