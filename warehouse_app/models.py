from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    cap = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name + self.city

    def get_absolute_url(self):
        return reverse('place_detail', kwargs={"pk": self.pk})


    class Meta:
        ordering = ['id']

class DeviceUser(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={"pk": self.pk})

    class Meta:
        ordering = ['id']


class Device(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    place = models.ForeignKey(Place, related_name="place", on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(DeviceUser, related_name="deviceuser", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_detail', kwargs={"pk": self.pk})
