from django.http import HttpResponse
import datetime

from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')

def notifications(request, pk):
    return render(request, 'notifications.html', {'pk': pk})


