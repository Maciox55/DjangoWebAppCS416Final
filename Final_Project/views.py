from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return render(request,'index.html')


def shipments(request):
    template = loader.get_template('shipments.html')
    return render(request,'shipments.html')


def shipment(request,shipment):
    template = loader.get_template('shipment.html')
    return render(request,'shipment.html')


def archive(request):
    template = loader.get_template('archive.html')
    return render(request,'archive.html')


def login(request):
    template = loader.get_template('login.html')
    return render(request,'login.html')