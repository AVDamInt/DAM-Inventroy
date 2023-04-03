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
    EXABYTE = 'EB'
    PETABYTE = 'PB'
    TERABYTE = 'TB'
    GIGABYTE = 'GB'
    MEGABYTE = 'MB'
    KILOBYTE = 'kB'
    BYTE = 'B'
    BIT = 'bit'
    UNIT_OF_MEASURE_CHOICES = [
        (EXABYTE, 'Exabyte'),
        (PETABYTE, 'Petabyte'),
        (TERABYTE, 'Terabyte'),
        (GIGABYTE, 'Gigabyte'),
        (MEGABYTE, 'Megabyte'),
        (KILOBYTE, 'Kilobyte'),
        (BIT, 'Bit')
    ]

    IS_AVAILABLE_CHOICES = [
        (0, 'Available'),
        (1, 'Unavailable')
    ]

    IS_HISTORY_CHOICES = [
        (0, 'Storico'),
        (1, 'Attivo')
    ]

    serial_number = models.CharField(max_length=50, blank=True, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    memory_unit = models.CharField(max_length=3, choices=UNIT_OF_MEASURE_CHOICES, default=GIGABYTE, blank=True,
                                   null=True)
    hard_disk = models.IntegerField(blank=True, null=True)
    hard_disk_unit = models.CharField(max_length=3, choices=UNIT_OF_MEASURE_CHOICES, default=GIGABYTE, blank=True,
                                      null=True)
    cpu = models.CharField(max_length=50, blank=True, null=True)
    place = models.ForeignKey(Place, related_name="place", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(DeviceUser, related_name="deviceuser", on_delete=models.CASCADE, blank=True, null=True)
    user_history = models.ManyToManyField(DeviceUser, blank=True, null=True)
    status = models.IntegerField(choices=IS_AVAILABLE_CHOICES, default=0, blank=True, null=True)
    history_type = models.IntegerField(choices=IS_HISTORY_CHOICES, default=0, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.contract

    def get_absolute_url(self):
        return reverse('device_detail', kwargs={"pk": self.pk})

    class Meta:
        ordering = ['id']
