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
    no=models.PositiveIntegerField()
    account=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False,related_name='account')
    particulars=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False,related_name='particulars')
    amount=models.IntegerField()
    def __str__(self):
     return self. account




