from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Final_Project.models import Shipment, ShipmentForm, Client


def index(request):
    template = loader.get_template('index.html')
    return render(request,'index.html')


@login_required
def shipments(request):
    template = loader.get_template('shipments.html')
    packaged = Shipment.objects.filter(user=request.user)
    clients = Client.objects.all()
    context = {'shipments' : packaged, 'clients':clients}

    if request.method == 'POST':
        form = ShipmentForm(request.POST or None)

        if form.is_valid():

            form.save()
            return redirect('shipments')
        else:
            return HttpResponse(form.errors)

    return render(request, 'shipments.html', context)


@login_required
def shipment(request, shipment):
    form = ShipmentForm
    return render(request, 'shipment.html')


@login_required
def archive(request):
    template = loader.get_template('archive.html')
    return render(request, 'archive.html')


@login_required
def archive(request):
    template = loader.get_template('archive.html')
    return render(request, 'archive.html')


@login_required
def manage(request):
    template = loader.get_template('manage.html')
    return render(request, 'manage.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
        else:
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request,'registration/register.html',context)


def login(request):
    template = loader.get_template('registration/login.html')

    return render(request, 'registration/login.html')