from django.contrib import admin
from tallyapp.models import groups,ledger,contra

# Register your models here.

admin.site.register(groups)

admin.site.register(ledger)

admin.site.register(contra)
