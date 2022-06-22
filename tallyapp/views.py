from django.shortcuts import render,redirect
from .models import GroupModel,LedgerModel,contra

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    if request.method=='POST':
        date=request.POST['date']
        no=request.POST['no']
        a=request.POST['account']
        account1=GroupModel.objects.get(id=a)
        b=request.POST['particulars']
        particular1=LedgerModel.objects.get(id=b)
        amount = request.POST['amount']
        con=contra(date=date,
                    no=no,
                    account=account1,
                    particulars=particular1,
                    amount=amount)
        con.save()
        print("hii")
        return redirect('/')
    return render(request,'page1.html')
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
