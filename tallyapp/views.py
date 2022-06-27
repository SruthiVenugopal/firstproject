from django.shortcuts import render,redirect
from .models import GroupModel,LedgerModel,contra
from datetime import datetime,date

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    conled=LedgerModel.objects.all()
    context={'conled':conled}
    if request.method=='POST':
        date=request.POST['date']
        no=request.POST['no']
        #transactiontype=request.POST['transactiontype']
        a=request.POST['account']
        account1=LedgerModel.objects.get(id=a)
        b=request.POST['particulars']
        particular1=LedgerModel.objects.get(id=b)
        amount = request.POST['amount']
        #narration=request.POST['narration']
        try:
            con=contra.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=contra(date=date,
                    no=no,
                    #transactiontype=transactiontype,
                    #narration=narration
                    account=account1,
                    particulars=particular1,
                    amount=amount)
                    
        con.save()
        print("hii")
        #return redirect('editcon')
    return render(request,'page1.html',context)

def editcon(request,pk):
    con=contra.objects.get(id=pk)
    context={'con':con}
    return render(request,'editcon.html',context)

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
    con=contra.objects.all()
    context={'con':con}
    return render(request,'daybook.html',context)
