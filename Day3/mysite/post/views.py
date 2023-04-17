from django.shortcuts import render

# Create your views here.

def viewAll(request):
    return render(request,'index.html')

def postHome(request):
    return render(request,'message.html')
