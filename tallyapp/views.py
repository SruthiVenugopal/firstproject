from django.shortcuts import render,redirect
from .models import Ledger,contra,payment,receipt,journal
from datetime import datetime,date

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    conled=Ledger.objects.filter(group_under='bankaccounts')
    context1={'conled':conled}
    if request.method =='POST':
        a=request.POST['account']
        b=Ledger.objects.get(id=a)
        c=request.POST['particulars']
        d=Ledger.objects.get(id=c)
        amount = request.POST['amount']
        narration=request.POST['narration']
        try:
            con=contra.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=contra(#date=date,
                    narration=narration,
                    no=no,
                    account=b,
                    particulars=d,
                    amount=amount)
                    
        con.save()
        print("hii")
        con=con.id
        return redirect('editcon',con)
    return render(request,'page1.html',context1)

def editcon(request,pk):
    con=contra.objects.get(id=pk)
    if  request.method=='POST':
        con = contra.objects.get(id=pk)
        con.transactiontype = request.POST.get('transactiontype')
        if con.transactiontype =="ATM":
            con.instno=5657
            con.instdate="25Mar2022"
            con.save()
        return redirect('index')
    return render(request, 'editcon.html',{'con':con})

def pay(request):
    payacc=Ledger.objects.filter(group_under='bankaccounts')
    payled=Ledger.objects.filter(group_under='paymentledger')
    context1={'payacc':payacc,'payled':payled}
    if request.method =='POST':
        a=request.POST['account']
        b=Ledger.objects.get(id=a)
        c=request.POST['particulars']
        d=Ledger.objects.get(id=c)
        amount = request.POST['amount']
        narration=request.POST['narration']
        try:
            con=payment.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=payment(#date=date,
                    narration=narration,
                    no=no,
                    account=b,
                    particulars=d,
                    amount=amount)
                    
        con.save()
        print("hii")
        con=con.id
        return redirect('editpay',con)
    return render(request,'payment.html',context1)

def editpay(request,pk):
    con=payment.objects.get(id=pk)
    if  request.method=='POST':
        con = payment.objects.get(id=pk)
        con.transactiontype = request.POST.get('transactiontype')
        if con.transactiontype =="ATM":
            con.instno=5657
            con.instdate="25Mar2022"
            con.save()
            return redirect('index')
    return render(request, 'editpay.html',{'con':con})

def rec(request):
    recacc=Ledger.objects.filter(group_under='bankaccounts')
    recled=Ledger.objects.filter(group_under='receiptledger')
    context1={'recacc':recacc,'recled':recled}
    if request.method =='POST':
        a=request.POST['account']
        b=Ledger.objects.get(id=a)
        c=request.POST['particulars']
        d=Ledger.objects.get(id=c)
        amount = request.POST['amount']
        narration=request.POST['narration']
        try:
            con=receipt.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=receipt(#date=date,
                    narration=narration,
                    no=no,
                    account=b,
                    particulars=d,
                    amount=amount)
                    
        con.save()
        print("hii")
        con=con.id
        return redirect('editrec',con)
    return render(request,'receipt.html',context1)

def editrec(request,pk):
    con=receipt.objects.get(id=pk)
    if  request.method=='POST':
        con = receipt.objects.get(id=pk)
        con.transactiontype = request.POST.get('transactiontype')
        if con.transactiontype =="ATM":
            con.instno=5657
            con.instdate="25Mar2022"
            con.save()
            return redirect('index')
    return render(request, 'editrec.html',{'con':con})

def jou(request):
    jouacc=Ledger.objects.filter(group_under='bankaccounts')
    jouled=Ledger.objects.filter(group_under='receiptledger')
    context1={'jouacc':jouacc,'jouled':jouled}
    if request.method =='POST':
        a=request.POST['account']
        b=Ledger.objects.get(id=a)
        c=request.POST['particulars']
        d=Ledger.objects.get(id=c)
        amount = request.POST['amount']
        narration=request.POST['narration']
        try:
            con=journal.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=journal(#date=date,
                    narration=narration,
                    no=no,
                    account=b,
                    particulars=d,
                    amount=amount)
                    
        con.save()
        print("hii")
        con=con.id
        return redirect('editjou',con)
    return render(request,'journal.html',context1)

def editjou(request,pk):
    con=journal.objects.get(id=pk)
    if  request.method=='POST':
        con = journal.objects.get(id=pk)
        con.transactiontype = request.POST.get('transactiontype')
        if con.transactiontype =="ATM":
            con.instno=5657
            con.instdate="25Mar2022"
            con.save()
        return redirect('index')
    return render(request, 'editjou.html',{'con':con})

def sal(request):
    salacc=Ledger.objects.filter(group_under='bankaccounts')
    salled=Ledger.objects.filter(group_under='receiptledger')
    context1={'salacc':salacc,'salled':salled}
    if request.method =='POST':
        a=request.POST['account']
        b=Ledger.objects.get(id=a)
        c=request.POST['particulars']
        d=Ledger.objects.get(id=c)
        rate=request.POST['rate']
        quantity=request.POST['quantity']
        narration=request.POST['narration']
        amount=rate*quantity
        try:
            con=journal.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=sales(#date=date,
                    narration=narration,
                    no=no,
                    account=b,
                    particulars=d,
                    rate=rate,
                    quantity=quantity)
                    
        con.save()
        print("hii")
        con=con.id
        return redirect('/')
    return render(request,'sales.html',context1)
def pur(request):
    return render(request,'purchase.html')
def daybook(request):
    # if request.method=="POST":
    #     fromdate=request.POST.get('fromdate')
    #     todate=request.POST.get('todate')
    #     searchresult=
    con=contra.objects.all()
    pay=payment.objects.all()
    rec=receipt.objects.all()
    jou=journal.objects.all()
    sal=sales.objects.all()
    pur=purchase.objects.all()
    context={'con':con,'pay':pay,'rec':rec,'jou':jou,'sal':sal,'pur':pur}
    return render(request,'daybook.html',context)
def daybookcon(request):
    con=contra.objects.all()
    context={'con':con}
    return render(request,'daybookcon.html',context)
def daybookpay(request):
    pay=payment.objects.all()
    context={'pay':pay}
    return render(request,'daybookpay.html',context)
def daybookrec(request):
    rec=receipt.objects.all()
    context={'rec':rec}
    return render(request,'daybookrec.html',context)
def daybookjou(request):
    jou=journal.objects.all()
    context={'jou':jou}
    return render(request,'daybookjou.html',context)
def delcon(request,pk):
    a=contra.objects.get(id=pk)
    a.delete()
    return redirect('daybook')
def delpay(request,pk):
    a=payment.objects.get(id=pk)
    a.delete()
    return redirect('daybook')
def delrec(request,pk):
    a=receipt.objects.get(id=pk)
    a.delete()
    return redirect('daybook')
def deljou(request,pk):
    a=journal.objects.get(id=pk)
    a.delete()
    return redirect('daybook')