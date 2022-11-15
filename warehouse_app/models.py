from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    contract = models.CharField(max_length=50)
    expiration_date = models.DateField()
    renewal_date = models.DateField()
    host_name = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('device_detail', kwargs={"pk": self.pk})