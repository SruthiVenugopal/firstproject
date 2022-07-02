from django.contrib import admin
from tallyapp.models import Ledger,contra,payment,receipt,journal

# Register your models here.

admin.site.register(Ledger)

admin.site.register(contra)

admin.site.register(payment)

admin.site.register(receipt)

admin.site.register(journal)
