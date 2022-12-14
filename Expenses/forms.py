from django.contrib.auth.models import User
from .models import Expenses
from django import forms

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['Name','Expense','Amount','Date']
