from django.shortcuts import render
from django.db.models import Sum
from Banking.models import Banking, Withdraw

# Create your views here.

def Das_View(request):
    bank = Banking.objects.aggregate(bank1 = Sum('Balance'))
    with_d = Withdraw.objects.all()
    wi = with_d[len(with_d)-1]
    
    print(with_d)
    
    return render(request,'Dashboard/dash.html',{'bank':bank,'wi':wi})
    
    