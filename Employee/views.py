from django.shortcuts import render, redirect
from Employee.models import Employee
from Employee.forms import EmployeeForm


def employee_register(request):
    empDict = {
        'empForm': EmployeeForm()
    }
    if request.method == 'POST':
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            empForm.save(commit=True)
        else:
            print(empForm.errors)
    return render(request, 'Employee/add_employee.html', context = empDict)


def employee_view(request):
    employees = Employee.objects.all().filter()
    return render(request,'Employee/employee.html', {'employees': employees})


def delete_employee(request, pk):
    employees = Employee.objects.get(id = pk)
    employees.delete()
    return employee_view(request)

def update_employee(request, pk):
    employee = Employee.objects.get(id = pk)
    employeeForm = EmployeeForm(instance = employee)
    employee_dict = {
        'empForm':employeeForm
    }

    if request.method=='POST':
        employeeForm = EmployeeForm(request.POST, instance = employee)

        if employeeForm.is_valid():
            employee = employeeForm.save(commit=True)
            employee.save()
        else:
            print(employeeForm.errors)
    return render(request, 'Employee/update_employee.html', context = employee_dict)


def search_employee_view(request):
        
    employees = ""
    
    if request.GET.get("query"):
        employees = Employee.objects.filter(PhoneNo = request.GET.get("query"))
    return render(request, 'Employee/employee.html', {'employees': employees})

