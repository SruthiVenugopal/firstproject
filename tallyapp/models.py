from pyexpat import model
from django.db import models

# Create your models here.


class groups(models.Model):
    group=models.CharField(max_length=225)


    def _str_(self):
     return self.group

class ledger(models.Model):
    group=models.ForeignKey(groups,on_delete=models.CASCADE,blank=False)
    name=models.CharField(max_length=225)

    def _str_(self):
     return self.name

class contra(models.Model):
    date=models.DateField(auto_now=True)
    no=models.IntegerField()
    accountchoice= [
        ('Cash', 'Cash'),
        ('Hdfc bank', 'Hdfc Bank'),
        ('Federal bank', 'Federal bank'),
        ('Sbi bank', 'Sbi bank'),
        ('Axis bank', 'Axis bank'),
        ('Bank of baroda', 'Bank if baroda'),
        ('Union bank', 'Union bank'),
        ('Uco bank', 'Uco bank')
        ]

    account=models.CharField(max_length=30,choices=accountchoice,default='cash')
    Particulars=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField()
    def __str__(self):
     return self. account




