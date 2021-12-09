from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from Final_Project.models import Shipment, ShipmentForm, Client, ClientForm

def index(request):
    template = loader.get_template('index.html')
    return render(request,'index.html')

def notfound(request):
    template = loader.get_template('404.html')
    return render(request,'404.html')


@login_required
def shipments(request):
    template = loader.get_template('shipments.html')

    if (request.user.is_superuser):
        packaged = Shipment.objects.filter(processed=False)
    else:
        packaged = Shipment.objects.filter(user=request.user, processed=False)
    clients = Client.objects.all()
    context = {'shipments': packaged, 'clients': clients}

    if request.method == 'POST':
        form = ShipmentForm(request.POST or None)
        client = get_object_or_404(Client, id=request.POST.get('client'))
        form.client = client
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
    template = loader.get_template('shipments.html')
    packaged = Shipment.objects.filter(user=request.user, processed=True)
    clients = Client.objects.all()
    context = {'shipments': packaged, 'clients': clients}
    return render(request, 'archive.html',context)




@login_required
def manage(request):
    clients = Client.objects.all()
    form = ClientForm(request.POST)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage')

    context = {'form': form, 'clients': clients}
    return render(request, 'manage.html', context)


@login_required
def editClient(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, initial={'id': client.id, 'name': client.name, 'streetNumber': client.streetNumber, 'streetName': client.streetName,
            'city': client.city, 'state': client.state, 'zip': client.zip})
    context = {'form': form}
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()

            return redirect('manage')

    return render(request, 'updateClient.html', context)


@login_required
def deleteClient(request,id):
    client = Client.objects.get(id=id)
    clients = Client.objects.all()
    form = ClientForm(request.POST)
    client.delete()

    context = {'form': form, 'clients': clients}
    return render(request, 'manage.html', context)



def register(request):
    form = UserCreationForm(request.POST)
    context = {'form': form}
    if request.method == 'POST':

        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)

            dj_login(request,user)
            return redirect('index')
        else:
            return render(request, 'registration/register.html', context)

    return render(request, 'registration/register.html', context)


def login(request):
    return render(request, 'registration/login.html')
