from django.contrib import admin

# Register your models here.
from .models import Device
from .models import Place
from .models import DeviceUser

admin.site.register(Device)
admin.site.register(Place)
admin.site.register(DeviceUser)