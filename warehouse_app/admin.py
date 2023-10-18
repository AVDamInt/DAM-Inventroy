from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Register your models here.
from .models import Device
from .models import Place
from .models import DeviceUser
from .models import Department
from .models import Office
from .models import Company
from django import forms

admin.site.register(Device)
admin.site.register(Place)
admin.site.register(DeviceUser)
admin.site.register(Department)
admin.site.register(Office)
admin.site.register(Company)