from django.contrib import admin
from tallyapp.models import GroupModel,LedgerModel,contra

# Register your models here.

admin.site.register(GroupModel)

admin.site.register(LedgerModel)

admin.site.register(contra)

#admin.site.register(payment)

# admin.site.register(receipt)

# admin.site.register(journal)
