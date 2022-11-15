from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    cap = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.SET_NULL)
    


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('device_detail', kwargs={"pk": self.pk})

