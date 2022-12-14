from django.db import models
from django.utils import timezone


class Expenses(models.Model):

    type = [('Salary','Salary'),
    ('Rent','Rent'),
    ('Maintence','Manitence'),
    ('Transport','Transport')]



    Name = models.CharField(max_length = 50)
    Expense = models.CharField(max_length = 20, choices= type)
    Amount = models.IntegerField()
    Date = models.DateField(default=timezone.now)

