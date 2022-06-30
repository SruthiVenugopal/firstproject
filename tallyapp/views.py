from django.shortcuts import render,redirect
from .models import GroupModel,LedgerModel,contra
from datetime import datetime,date

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    a=GroupModel.objects.get(name="bankaccounts")
    conled=LedgerModel.objects.filter(group=a.id)
    context1={'conled':conled}
    if request.method=='POST':
        #date=request.POST['date']
        #no=request.POST['no']
        #transactiontype=request.POST['transactiontype']
        a=request.POST['account']
        account1=LedgerModel.objects.filter(ledger_name=a).first()
        b=request.POST['particulars']
        particular1=LedgerModel.objects.filter(ledger_name=b).first()
        amount = request.POST['amount']
        narration=request.POST['narration']
        try:
            con=contra.objects.all().last()
            no=con.no+1
        except:
            no=1
        con=contra(date=date,
                    no=no,
                    account=account1,
                    particulars=particular1,
                    amount=amount)
                    
        con.save()
        print("hii")
        context2={'account1':account1,'particular1':particular1,'amount':amount,'narration':narration}
        return render(request,'editcon.html',context2)
    return render(request,'page1.html',context1)

# def payment(request):
#     payled=LedgerModel.objects.all()
#     context1={'payled':payled}
#     if request.method=='POST':
#         #date=request.POST['date']
#         #no=request.POST['no']
#         a=request.POST['account']
#         account1=LedgerModel.objects.get(id=a)
#         b=request.POST['particulars']
#         particular1=LedgerModel.objects.get(id=b)
#         amount = request.POST['amount']
#         narration=request.POST['narration']
#         try:
#             pay=payment.objects.all().last()
#             no=pay.no+1
#         except:
#             no=1
#         pay=payment(date=date,
#                     no=no,
#                     account=account1,
#                     particulars=particular1,
#                     amount=amount)
                    
#         pay.save()
#         print("hii")
#         context2={'account1':account1,'particular1':particular1,'amount':amount,'narration':narration}
#         return render(request,'editpay.html',context2)
#     return render(request,'payment.html',context1)
# def receipt(request):
#     recled=LedgerModel.objects.all()
#     context1={'recled':recled}
#     if request.method=='POST':
#         date=request.POST['date']
#         no=request.POST['no']
#         a=request.POST['account']
#         account1=LedgerModel.objects.get(id=a)
#         b=request.POST['particulars']
#         particular1=LedgerModel.objects.get(id=b)
#         amount = request.POST['amount']
#         narration=request.POST['narration']
#         try:
#             rec=receipt.objects.all().last()
#             no=rec.no+1
#         except:
#             no=1
#         rec=receipt(date=date,
#                     no=no,
#                     account=account1,
#                     particulars=particular1,
#                     amount=amount)
                    
#         rec.save()
#         print("hii")
#         context2={'account1':account1,'particular1':particular1,'amount':amount,'narration':narration}
#         return render(request,'editrec.html',context2)
#     return render(request,'receipt.html',context1)
# def journal(request):
#     jouled=LedgerModel.objects.all()
#     context1={'jouled':jouled}
#     if request.method=='POST':
#         date=request.POST['date']
#         no=request.POST['no']
#         a=request.POST['account']
#         account1=LedgerModel.objects.get(id=a)
#         b=request.POST['particulars']
#         particular1=LedgerModel.objects.get(id=b)
#         amount = request.POST['amount']
#         narration=request.POST['narration']
#         try:
#             jou=journal.objects.all().last()
#             no=jou.no+1
#         except:
#             no=1
#         jou=journal(date=date,
#                     no=no,
#                     account=account1,
#                     particulars=particular1,
#                     amount=amount)
                    
#         jou.save()
#         print("hii")
#         context2={'account1':account1,'particular1':particular1,'amount':amount,'narration':narration}
#         return render(request,'editcon.html',context2)
#     return render(request,'journal.html',context1)
# def sales(request):
#     return render(request,'sales.html')
# def purchase(request):
#     return render(request,'purchase.html')
# def daybook(request):
#     con=contra.objects.all()
#     pay=payment.objects.all()
#     rec=receipt.objects.all()
#     jou=journal.objects.all()
#     context={'con':con,'pay':pay,'rec':rec,'jou':jou}
#     return render(request,'daybook.html',context)
# def daybookcon(request):
#     con=contra.objects.all()
#     context={'con':con}
#     return render(request,'daybookcon.html',context)
# def daybookpay(request):
#     pay=payment.objects.all()
#     context={'pay':pay}
#     return render(request,'daybookpay.html',context)
# def daybookrec(request):
#     rec=receipt.objects.all()
#     context={'rec':rec}
#     return render(request,'daybookrec.html',context)
# def daybookjou(request):
#     jou=journal.objects.all()
#     context={'jou':jou}
#     return render(request,'daybookjou.html',context)
# def delcon(request,pk):
#     a=contra.objects.get(id=pk)
#     a.delete()
#     return redirect('daybook')
# def delpay(request,pk):
#     a=payment.objects.get(id=pk)
#     a.delete()
#     return redirect('daybook')
# def delrec(request,pk):
#     a=receipt.objects.get(id=pk)
#     a.delete()
#     return redirect('daybook')
# def deljou(request,pk):
#     a=journal.objects.get(id=pk)
#     a.delete()
#     return redirect('daybook')