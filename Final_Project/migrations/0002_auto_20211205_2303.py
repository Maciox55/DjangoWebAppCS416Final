# Generated by Django 3.2.9 on 2021-12-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='date_processed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='date_shipping',
            field=models.DateField(null=True),
        ),
    ]