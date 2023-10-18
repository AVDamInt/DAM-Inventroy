from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Place(models.Model):
    # Nome del luogo
    name = models.CharField(max_length=50, default='Empty')
    city = models.CharField(max_length=50, default='Empty')
    address = models.CharField(max_length=50, blank=True, null=True)
    cap = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]

class Office(models.Model):
    # UFFICIO
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("office_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]

class Department(models.Model):
    # DIREZIONE
    name = models.CharField(max_length=50, null=True)
    # one to many su Office
    #office = models.ForeignKey(Office, related_name="office", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]


class DeviceUser(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    # Retrive email from azure/active directrory?
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]


class Company(models.Model):
    # COMPANY
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]

def get_foo():
    return Company.objects.get_or_create(id=1)

class Device(models.Model):
    EXABYTE = "EB"
    PETABYTE = "PB"
    TERABYTE = "TB"
    GIGABYTE = "GB"
    MEGABYTE = "MB"
    KILOBYTE = "kB"
    BYTE = "B"
    BIT = "bit"
    UNIT_OF_MEASURE_CHOICES = [
        (EXABYTE, "Exabyte"),
        (PETABYTE, "Petabyte"),
        (TERABYTE, "Terabyte"),
        (GIGABYTE, "Gigabyte"),
        (MEGABYTE, "Megabyte"),
        (KILOBYTE, "Kilobyte"),
        (BIT, "Bit"),
    ]

    company = models.ForeignKey(Company, on_delete=models.SET_DEFAULT, default=get_foo)

    # Populated by USER field with DISPONIBILE value Default = Available -> Indicates whether the product is available or assigned to an user
    IS_AVAILABLE_CHOICES = [(0, "Available"), (1, "Unavailable")]

    # STATO
    IS_HISTORY_CHOICES = [(0, "Storico"), (1, "Attivo")]

    # MATRICOLA
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    # CONTR
    contract = models.CharField(max_length=50, null=True)
    # SCAD
    expiration_date = models.DateField(null=True)
    # RINNOVO
    renewal_date = models.DateField(blank=True, null=True)
    # HOST_NAME
    host_name = models.CharField(max_length=50, blank=True, null=True)
    # MARCA
    make = models.CharField(max_length=50, null=True)
    # TYPE
    model = models.CharField(max_length=50, blank=True, null=True)

    # New device_type = DESC = FOREING KEY TO NEW MODEL obbligatorio
    # device_type = ...
    # RAM
    memory = models.IntegerField(blank=True, null=True)
    memory_unit = models.CharField(
        max_length=3,
        choices=UNIT_OF_MEASURE_CHOICES,
        default=GIGABYTE,
        blank=True,
        null=True,
    )
    # HDD
    hard_disk = models.IntegerField(blank=True, null=True)
    hard_disk_unit = models.CharField(
        max_length=3,
        choices=UNIT_OF_MEASURE_CHOICES,
        default=GIGABYTE,
        blank=True,
        null=True,
    )

    # Not available in current inventory
    cpu = models.CharField(max_length=50, blank=True, null=True)

    place = models.ForeignKey(
        Place, related_name="place", on_delete=models.SET_NULL, null=True
    )

    # IPADDRESS default = set to DHCP
    addr_ip = models.CharField(max_length=12, null=True, default="DHCP")
    user = models.ForeignKey(
        DeviceUser,
        related_name="deviceuser",
        on_delete=models.SET_NULL,
        null=True,
    )
    user_history = models.ManyToManyField(DeviceUser, blank=True, null=True)
    status = models.IntegerField(
        choices=IS_AVAILABLE_CHOICES, default=0, null=True
    )
    history_type = models.IntegerField(
        choices=IS_HISTORY_CHOICES, default=0, null=True
    )
    note = models.TextField(max_length=400, blank=True, null=True)

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.contract

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["id"]


