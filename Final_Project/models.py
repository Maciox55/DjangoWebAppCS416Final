from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(max_length=200,null=True)
    streetNumber = models.CharField(max_length=200,null=True)
    streetName = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zip = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=200)

    def __str__(self):
        return self.serial_number


class Shipment(models.Model):
    #user = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client = models.CharField(max_length=200, blank=True)
    shipping_vendor = models.CharField(max_length=200, blank=True)
    part_number = models.CharField(max_length=200, blank=True)
    work_order = models.CharField(max_length=200, blank=True)
    sales_order = models.CharField(max_length=200, blank=True)
    qnt = models.CharField(max_length=200, editable=True)
    #serial_numbers = models.ForeignKey(SerialNumber, on_delete=models.CASCADE)
    serial_numbers = models.CharField(max_length=2000)
    processed = models.BooleanField(default=False)
    palletized = models.BooleanField(default=False)
    width = models.CharField(max_length=200, editable=True)
    length = models.CharField(max_length=200, editable=True)
    height = models.CharField(max_length=200, editable=True)
    weight = models.CharField(max_length=200, editable=True)
    date_created = models.DateTimeField(default=now, editable=False)
    date_processed = models.DateTimeField(null=True)
    date_shipping = models.DateField(null=True)

    def __str__(self):
        return self.client + self.work_order


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = ['user', 'client', 'shipping_vendor', 'part_number',
                  'work_order', 'qnt', 'serial_numbers', 'processed', 'palletized',
                  'width','length','height','weight']
