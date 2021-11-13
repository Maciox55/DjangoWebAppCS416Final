from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader



def index(request):
    template = loader.get_template('index.html')

    return render(request,'index.html')

def shipments(request):
    return HttpResponse("Hello, World. This is shipments!")

def shipment(request,shipment):
    return HttpResponse("Hello, World. This is a "+shipment+" !")
