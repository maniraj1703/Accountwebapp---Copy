from django.contrib import admin
from Banking.models import Banking, Amount, Vendor, Customer

# Register your models here.

admin.site.register(Banking)
admin.site.register(Amount)
admin.site.register(Vendor)
admin.site.register(Customer)