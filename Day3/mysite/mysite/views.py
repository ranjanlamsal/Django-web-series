from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Hello World!!!!</h1><h2>Hello world again!!<h2/></body></html>"
    return HttpResponse(html)

def message(request):

    html = "<html><body><h1>Your Message</h1><h2>Hello world again!!<h2/></body></html>"
    return HttpResponse(html)

def notifications(request):

    html = "<html><body><h1>Your Notifications</h1><h2>Hello world again!!<h2/></body></html>"
    return HttpResponse(html)
