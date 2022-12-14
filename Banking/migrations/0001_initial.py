# Generated by Django 4.1.4 on 2022-12-07 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Number', models.IntegerField()),
                ('IFSC_Number', models.CharField(max_length=10)),
                ('Holder_Name', models.CharField(max_length=25)),
                ('Money', models.IntegerField()),
                ('Note', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Amount',
            },
        ),
        migrations.CreateModel(
            name='Banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_Name', models.CharField(max_length=30)),
                ('IFSC_Number', models.CharField(max_length=10)),
                ('Account_Number', models.IntegerField()),
                ('Holder_Name', models.CharField(max_length=25)),
                ('Mobile_Number', models.IntegerField()),
                ('Balance', models.IntegerField()),
            ],
            options={
                'db_table': 'Banking',
            },
        ),
        migrations.CreateModel(
            name='Credit_Amount',
            fields=[
                ('S_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Current_Balance', models.IntegerField()),
                ('Acc_Num', models.IntegerField()),
                ('Credit', models.IntegerField()),
                ('Date', models.DateField(default=datetime.datetime(2022, 12, 7, 8, 22, 12, 995591))),
            ],
            options={
                'db_table': 'Credit_Amount',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_Name', models.CharField(max_length=30)),
                ('IFSC_Number', models.CharField(max_length=10)),
                ('Account_Number', models.IntegerField()),
                ('Holder_Name', models.CharField(max_length=25)),
                ('Mobile_Number', models.IntegerField()),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_Name', models.CharField(max_length=30)),
                ('IFSC_Number', models.CharField(max_length=10)),
                ('Account_Number', models.IntegerField()),
                ('Holder_Name', models.CharField(max_length=25)),
                ('Mobile_Number', models.IntegerField()),
            ],
            options={
                'db_table': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('S_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Current_Balance', models.IntegerField()),
                ('Acc_Num', models.IntegerField()),
                ('Debit', models.IntegerField()),
                ('Date', models.DateField(default=datetime.datetime(2022, 12, 7, 8, 22, 12, 994592))),
            ],
            options={
                'db_table': 'Withdraw',
            },
        ),
    ]