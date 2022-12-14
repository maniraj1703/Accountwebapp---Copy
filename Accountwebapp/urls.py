"""Accountwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Employee import views as empView
from Banking import views as bnkView
from .views import home_view
from Sales import views as saleview
from Purchase import views as bilview
from Purchase import views as ordview
from Purchase import views as venview
from Expenses import views as expview
from Reports import views as repview
from Reports import views as exview
from UserManager import views as userView
from . import views
from django.contrib.auth import views as auth_views
from Dashboard import views as dasView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view),
    path('purchase/bills/', bilview.bills_view, name="bills"),
    path('delete-bill/<int:pk>', bilview.delete_bills, name='delete-bills'),
    path('update-bills/<int:pk>', bilview.update_bills, name='update-bills'),
    path('add_bills/', bilview.bills_register,name = 'add_bills'),
    path('searchbill/', bilview.search_bills_view),
    path('purchase/order/', ordview.orders_view, name="orders"),
    path('delete-orders/<int:pk>', ordview.delete_orders, name='delete-order'),
    path('update-orders/<int:pk>', ordview.update_orders, name='update-order'),
    path('add-order/', ordview.orders_register, name = 'add_order'),
    path('next/<int:pk>', ordview.orders_reg),
    path('searchorder/', ordview.search_order_view),
    path('purchase/vendor/', venview.vendor_view, name='pur_ven'),
    path('delete-vendor/<int:pk>', venview.delete_vendor, name='delete-vendor'),
    path('update-vendor/<int:pk>', venview.update_vendor, name='update-vendor'),
    path('add-vendor/', venview.vendor_register,name = 'add-vendor'),
    path('select_vendor/', ordview.vendor_display),
    path('searchvendor/', venview.search_vendor_view),
    path('Expenses/', expview.expenses_view),
    path('delete-expense/<int:pk>', expview.delete_expenses, name='delete-expenses'),
   
    path('add-expense/', expview.Expenses_register,name = 'add-expense'),
    path('searchexpense/', expview.search_expenses_view),
    path('Report/bills/',repview.bills_view),
    path('Report/exp/',exview.expense_view),
    path('Report/sale/',repview.sale_view),
    path('dashboard/', dasView.Das_View, name='dashboard'),
    path('Report/bank',repview.bank_view),

    path('login/', auth_views.LoginView.as_view(template_name='UserInterface/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Base/index.html'), name='logout'),
    
    path('signup/', userView.signup_view),

    
    path('employees/', empView.employee_view),
    path('delete-employee/<int:pk>', empView.delete_employee, name='delete-employee'),
    path('update-employee/<int:pk>', empView.update_employee, name='update-employee'),
    path('add-employee/', empView.employee_register, name = 'add-employee'),
    path('searchemployee/', empView.search_employee_view),
    path('customer/', saleview.customer_view),
    path('delete-customer/<int:pk>', saleview.delete_customer, name='delete-customer'),
    path('update-customer/<int:pk>', saleview.update_customer, name='update-customer'),
    path('add-Customer/', saleview.customer_register,name = 'add-Customer'),
    path('searchcustomer/', saleview.search_customer_view),
    path('salesorder/', saleview.salesorder_view),
    path('delete-salesorder/<int:pk>', saleview.delete_salesorder, name='delete-salesorder'),
    path('update-salesorder/<int:pk>', saleview.update_salesorder, name='update-salesorder'),
    path('add-salesorder/', saleview.SelectCustomerView.as_view(), name='select-supplier'),
    path('searchsalesorder/', saleview.search_salesorder_view),

    path('new-sales/', saleview.SalesView.as_view(), name='sales-list'), 
    path('new-sales/new', saleview.SelectCustomerView.as_view(), name='select-customer'),
    path('new-sales/new/<pk>', saleview.SalesCreateView.as_view(), name='new-customer-sales'),
    path('new-sales/<pk>/delete', saleview.SalesDeleteView.as_view(), name='delete-sales'),  
    # Banking
    path('banking/add_bank', bnkView.bank_view, name='bank'),
    path('banking/vendor_bank', bnkView.vend_view, name='vend_bank'),
    path('banking/customer_bank', bnkView.cus_view, name='cus_bank'),
    path('delete-bank/<int:id>', bnkView.delete_bank, name='delete-bank'),
    path('update-bank/<int:id>', bnkView.update_bank, name='update-bank'),
    path('add-bank/', bnkView.bank_register, name='add-bank'),
    path('add-amt-bank/<int:id>', bnkView.add_amt, name='add-amt-bank'),
    path('delete-vendor-bank/<int:id>', bnkView.delete_vendor, name='delete-vendor-bank'),
    path('update-vendor-bank/<int:id>', bnkView.update_vendor, name='update-vendor-bank'),
    path('add-vendor-bank/', bnkView.vendor_register, name='add-vendor-bank'),
    path('search_vendor_bank/', bnkView.search_vendor_view),
    path('delete-customer-bank/<int:id>', bnkView.delete_customer, name='delete-customer-bank'),
    path('update-customer-bank/<int:id>', bnkView.update_customer, name='update-customer-bank'),
    path('add-customer-bank/', bnkView.customer_register, name='add-customer-bank'),
    path('search_customer_bank/', bnkView.search_customer_view),
    path('banking/withdraw', bnkView.withdraw_view, name='withdraw_amt-bank'),
    path('choose-acc-bank/<int:id>', bnkView.choose_acc, name='choose-acc-bank'),
    path('with-amt-bank/<int:id>', bnkView.with_amt, name='with-amt-bank'),
    path('dashboard/', dasView.Das_View, name='dashboard'),

    path('purchase/bills/', bilview.bills_view),
    path('delete-bill/<int:pk>', bilview.delete_bills, name='delete-bills'),
    path('update-bill/<int:pk>', bilview.update_bills, name='update-bills'),
    path('add_bills/', bilview.bills_register,name = 'add_bills'),
    path('searchbill/', bilview.search_bills_view),
    path('purchase/order/', ordview.orders_view),
    path('delete-orders/<int:pk>', ordview.delete_orders, name='delete-orders'),
    path('update-order/<int:pk>', ordview.update_orders, name='update-orders'),
    path('add-order/', ordview.orders_register, name = 'add_order'),
    path('searchorder/', ordview.search_order_view),
    path('purchase/vendor/', venview.vendor_view),
    path('delete-vendor/<int:pk>', venview.delete_vendor, name='delete-vendor'),
    path('update-vendor/<int:pk>', venview.update_vendor, name='update-vendor'),
    path('add-vendor/', venview.vendor_register,name = 'add-vendor'),
    path('searchvendor/', venview.search_vendor_view),
]

# TODO
# Duplicate Product should not be added
# Auto Price Calculation
# Auto Phone number of vendor