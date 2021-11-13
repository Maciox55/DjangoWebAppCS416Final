from django.db import models


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

    def __str__(self):
        return self.client + self.work_order


    class Meta:
        ordering = ['name']