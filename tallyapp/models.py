from pyexpat import model
from django.db import models
from datetime import datetime

# Create your models here.

class GroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    gp_behaves_like_sub_ledger = models.BooleanField(default=False)
    nett_debit_credit_bal_reporting = models.BooleanField(default=False)
    used_for_calculation = models.BooleanField(default=False)
    method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
        return self.name

class LedgerModel(models.Model):
    #cid=models.ForeignKey(CompanyModel,on_delete=models.CASCADE,null=True,blank=True)
    ledger_name = models.CharField(max_length=225)
    ledger_alias = models.CharField(max_length=225)
    group = models.ForeignKey(
        GroupModel, on_delete=models.CASCADE, null=True, blank=True)

    ledger_opening_bal = models.CharField(max_length=225)
    ledger_type = models.CharField(max_length=225)
    type_of_duty = models.CharField(max_length=225)
    percent_of_calculation = models.CharField(max_length=225)
    maintain_bal_bill = models.CharField(max_length=225)
    credit_days_during_voucher_entry = models.CharField(max_length=225)
    default_cr_peroid = models.CharField(max_length=225)
    provide_banking_details = models.BooleanField()

    def __str__(self):
        return self.ledger_name

class contra(models.Model):
    
    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='accountled')
    particulars=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='partled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class payment(models.Model):

    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='accountled')
    particulars=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='partled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class receipt(models.Model):

    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='accountled')
    particulars=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='partled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account

class journal(models.Model):

    instno=models.PositiveIntegerField(default=5656,null=False)
    instdate=models.CharField(default='24Mar2022',null=False)
    date=models.DateField(auto_now=True)
    no=models.PositiveIntegerField(default=0,null=False)
    account=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='accountled')
    particulars=models.ForeignKey(LedgerModel,on_delete=models.CASCADE,blank=False,related_name='partled')
    amount=models.IntegerField()
    def __str__(self):
        if self.pk:
            self.no += 1
        return self. account





        




