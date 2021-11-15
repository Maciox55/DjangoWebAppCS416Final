from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request,'registration/register.html',context)


def login(request):
    template = loader.get_template('registration/login.html')

    return render(request, 'registration/login.html')