from django.shortcuts import render, redirect, get_object_or_404
from Sales.models import (
    CustomerDetails,
    SalesOrder,
    SalesBill,
    SalesBillDetails,
    SalesItem
)
from Sales.forms import (
    CustomerForm,
    SalesOrderForm,
    SelectCustomerForm,
    SalesItemFormset
)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from Sales.models import CustomerDetails,SalesOrder
from Sales.forms import CustomerForm,SalesOrderForm
from Purchase.models import Vendororder


#  --------------------------for Customer-----------------------------

def customer_register(request):
    cusDict = {
        'cusForm': CustomerForm()
    }
    if request.method == 'POST':
        cusForm = CustomerForm(request.POST)
        if cusForm.is_valid():
            cusForm.save(commit=True)
        else:
            print(cusForm.errors)
    return render(request, 'Sales/add_Customer.html', context = cusDict)


def customer_view(request):
    customer = CustomerDetails.objects.all().filter()
    return render(request,'Sales/customer.html', {'customer': customer})

def delete_customer(request, pk):
    customer = CustomerDetails.objects.get(id = pk)
    customer.delete()
    return customer_view(request)


def update_customer(request, pk):
    customer = CustomerDetails.objects.get(id = pk)
    customerForm = CustomerForm(instance = customer)

    customer_dict = {
        'cusForm': customerForm
    }

    if request.method=='POST':
        customerForm = CustomerForm(request.POST, instance = customer)

        if customerForm.is_valid():
            customer = customerForm.save(commit=True)
            customer.save()
        else:
            print(customerForm.errors)
    return render(request, 'Sales/update_customer.html', context = customer_dict)


def search_customer_view(request):
    customer = ""
    if request.GET.get("query"):
        customer = CustomerDetails.objects.filter(PhoneNo = request.GET.get("query"))
    return render(request, 'Sales/customer.html', {'customer': customer})

# used to view a customer's profile
class CustomerView(View):
    def get(self, request, name):
        customObj = get_object_or_404(CustomerDetails, name=name)
        bill_list = SalesBill.objects.filter(supplier=customObj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'customer'  : customObj,
            'bills'     : bills
        }
        return render(request, 'suppliers/supplier.html', context)

# shows the list of bills of all purchases 
class SalesView(ListView):
    model = SalesBill
    template_name = "sales/salesorder.html"
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10

class SelectCustomerView(View):
    form_class = SelectCustomerForm
    template_name = 'Sales/select_customer.html'

    def get(self, request, *args, **kwargs):                                    # loads the form page
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):                                   # gets selected supplier and redirects to 'SalesPurchaseCreateView' class
        form = self.form_class(request.POST)
        if form.is_valid():
            customerid = request.POST.get("customer")
            customer = get_object_or_404(CustomerDetails, id=customerid)
            return redirect('new-customer-sales', customer.pk)
        return render(request, self.template_name, {'form': form})

# used to generate a bill object and save items
class SalesCreateView(View):                                                 
    template_name = 'Sales/new_sales.html'

    def get(self, request, pk):
        formset = SalesItemFormset(request.GET or None)            # renders an empty formset
        customerObj = get_object_or_404(CustomerDetails, pk=pk)                        # gets the supplier object
        context = {
            'formset'   : formset,
            'supplier'  : customerObj,
        }                                                                       # sends the supplier and formset as context
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = SalesItemFormset(request.POST)                             # recieves a post method for the formset
        customerObj = get_object_or_404(CustomerDetails, pk=pk)                        # gets the supplier object
        if formset.is_valid():
            # saves bill
            billobj = SalesBill(customer=customerObj)                        # a new object of class 'PurchaseBill' is created with supplier field set to 'customerObj'
            billobj.save()                                                      # saves object into the db
            # create bill details object
            billdetailsobj = SalesBillDetails(billno=billobj)
            billdetailsobj.save()
            for form in formset:                                                # for loop to save each individual form as its own object
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)
                billitem.billno = billobj            
                print("billitem")                       # links the bill object to the items
                print(billitem)                       # links the bill object to the items
                stock = get_object_or_404(Vendororder, Product=billitem.stock.Product)      
                billitem.totalprice = billitem.perprice * billitem.quantity
                stock.Product_Quantity -= billitem.quantity
                stock.save() 
                billitem.save()
            messages.success(request, "Purchased items have been registered successfully")
            return redirect('sales-list')
        formset = SalesItemFormset(request.GET or None)
        context = {
            'formset'   : formset,
            'supplier'  : customerObj
        }
        return render(request, self.template_name, context)

# used to delete a bill object
class SalesDeleteView(SuccessMessageMixin, DeleteView):
    model = SalesBill
    template_name = "Sales/delete_sales.html"
    success_url = '/new-sales'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = SalesItem.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Vendororder, Product=item.stock.Product)
            if stock.is_deleted == False:
                stock.Product_Quantity += item.quantity
                stock.save()
        messages.success(self.request, "Sales bill has been deleted successfully")
        return super(SalesDeleteView, self).delete(*args, **kwargs)
# ------------------for SalesOrder-----------------------------

def salesorder_register(request):
    salDict = {
        'salForm': SalesOrderForm()
    }
    if request.method == 'POST':
        if 'search-customer' in request.POST:
            print('post')
            print(request.POST)
            if request.POST.get("CustomerPhoneNo"):
                customer = CustomerDetails.objects.filter(PhoneNo = request.GET.get("CustomerPhoneNo"))
                print(customer)
                return HttpResponseRedirect(reverse('Sales/add_salesorder.html'))
        else:
            salForm = SalesOrderForm(request.POST)
            if salForm.is_valid():
                salForm.save(commit=True)
            else:
                print(salForm.errors)
    return render(request, 'Sales/add_salesorder.html', context = salDict)


def salesorder_view(request):
    salesorder = SalesOrder.objects.all().filter()
    return render(request,'Sales/salesorder.html', {'salesorder': salesorder})

def delete_salesorder(request, pk):
    salesorder = SalesOrder.objects.get(id = pk)
    salesorder.delete()
    return salesorder_view(request)

def update_salesorder(request, pk):
    salesorder = SalesOrder.objects.get(id = pk)
    salesorderForm = SalesOrderForm(instance = salesorder)

    salesorder_dict = {
        'salForm': salesorderForm
    }

    if request.method=='POST':
        salesorderForm = SalesOrderForm(request.POST, instance = salesorder)

        if salesorderForm.is_valid():
            salesorder = salesorderForm.save(commit=True)
            salesorder.save()
        else:
            print(salesorderForm.errors)
    return render(request, 'Sales/update_salesorder.html', context = salesorder_dict)


def search_salesorder_view(request):
    salesorder = ""
    if request.GET.get("query"):
        salesorder = SalesOrder.objects.filter(CustomerPhoneNo = request.GET.get("query"))
    return render(request, 'Sales/salesorder.html', {'salesorder': salesorder})
