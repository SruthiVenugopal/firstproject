from django.contrib import admin
from tallyapp.models import Ledger,contra,payment,receipt,journal,sales,purchase

# Register your models here.

admin.site.register(Ledger)

admin.site.register(contra)

admin.site.register(payment)

admin.site.register(receipt)

admin.site.register(journal)

admin.site.register(sales)

admin.site.register(purchase)
