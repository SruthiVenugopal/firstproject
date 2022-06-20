from django.shortcuts import render,redirect
from .models import groups,ledger,contra

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    ledgers=ledger.objects.all()
    context1={'ledgers':ledgers}
    accledger=legder.objects.filter(group='bank accounts')
    context2={'accledger':accledger}
    if request.method=='POST':
        date=request.POST['date']
        no=request.POST['no']
        a=request.POST['account']
        account1=ledger.objects.get(id=a)
        b=request.POST['particulars']
        particular1=legder.objects.get(id=b)
        amount = request.POST['amount']
        con=contra(date=date,
                    no=no,
                    account=account1,
                    particulars=particular1,
                    amount=amount)
        con.save()
        print("hii")
        return redirect('/')
    return render(request,'page1.html',context1,context2)
def payment(request):
    return render(request,'payment.html')
def receipt(request):
    return render(request,'receipt.html')
def journal(request):
    return render(request,'journal.html')
def sales(request):
    return render(request,'sales.html')
def purchase(request):
    return render(request,'purchase.html')
def daybook(request):
    return render(request,'daybook.html')
