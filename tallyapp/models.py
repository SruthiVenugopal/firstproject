
from django.db import models
from datetime import datetime

# Create your models here.
class Ledger(models.Model):
    ledger_name = models.CharField(max_length=225)
    ledger_alias = models.CharField(max_length=225)
    group_under=models.CharField(max_length=225)
    ledger_opening_bal = models.CharField(max_length=225)
    ledger_type = models.CharField(max_length=225)
    provide_banking_details = models.CharField(max_length=225)

    def __str__(self):
        return self.ledger_name

class contra(models.Model):
    narration=models.CharField(max_length=30)
    transchoice=[
        ('cheque/dd', 'Cheque/dd'),
        ('atm', 'Atm'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('e-fund-transfer', 'E-fund-transfer'),
        ('others', 'Others')
        ]
    transactiontype=models.CharField(max_length=30,choices=transchoice,default='cheque/dd')
    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(max_length=225,default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='accountled')
    particulars=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='partled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class payment(models.Model):
    narration=models.CharField(max_length=30)
    transchoice=[
        ('cheque/dd', 'Cheque/dd'),
        ('atm', 'Atm'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('e-fund-transfer', 'E-fund-transfer'),
        ('others', 'Others')
        ]
    transactiontype=models.CharField(max_length=30,choices=transchoice,default='cheque/dd')
    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(max_length=255,default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='payacc')
    particulars=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='payled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class receipt(models.Model):
    narration=models.CharField(max_length=30)
    transchoice=[
        ('cheque/dd', 'Cheque/dd'),
        ('atm', 'Atm'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('e-fund-transfer', 'E-fund-transfer'),
        ('others', 'Others')
        ]
    transactiontype=models.CharField(max_length=30,choices=transchoice,default='cheque/dd')
    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(max_length=255,default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='recacc')
    particulars=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='recled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class journal(models.Model):
    transchoice=[
        ('cheque/dd', 'Cheque/dd'),
        ('atm', 'Atm'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('e-fund-transfer', 'E-fund-transfer'),
        ('others', 'Others')
        ]
    transactiontype=models.CharField(max_length=30,choices=transchoice,default='cheque/dd')
    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(max_length=255,default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='jouacc')
    particulars=models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=False,related_name='jouled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account





        




