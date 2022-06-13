from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def page1(request):
    return render(request,'page1.html')