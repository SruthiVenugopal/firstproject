from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
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
