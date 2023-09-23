from django.http import HttpResponse
from django.shortcuts import render
from .models import People

# Create your views here.

def home(request):
    data={}
    if request.method == "POST":
         a=request.POST.get("n1")
         b=request.POST.get("a1")
         d=request.POST.get("d1")


         data={
            'x' : a,
            'y' : b,
            'z' : d,
           }
         
         info=People()
         info.name=a
         info.address=b
         info.department=d
         info.save()
       
    return render(request,"form.html",data)