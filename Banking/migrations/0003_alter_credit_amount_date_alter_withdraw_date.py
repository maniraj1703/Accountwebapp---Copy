# Generated by Django 4.1.4 on 2022-12-07 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0002_alter_credit_amount_date_alter_withdraw_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit_amount',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 12, 7, 8, 59, 36, 930373)),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 12, 7, 8, 59, 36, 929374)),
        ),
    ]
