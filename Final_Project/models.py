from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=200)

    def __str__(self):
        return self.serial_number


class Shipment(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE())
    shipping_vendor = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    work_order = models.CharField(max_length=200)
    sales_order = models.CharField(max_length=200)
    quantity = models.IntegerField
    serial_numbers = models.ForeignKey(SerialNumber)
    processed = models.BooleanField
    palletized = models.BooleanField
    width = models.IntegerField
    length = models.IntegerField
    height = models.IntegerField
    date_created = models.DateTimeField(default=now, editable=False)
    date_processed = models.DateTimeField
    date_shipping = models.DateDield

    def __str__(self):
        return self.client + self.work_order

    class Meta:
        ordering = ['name']