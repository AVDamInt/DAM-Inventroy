from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

#def index(request):
#    return HttpResponse("Warehouse!")

def device_list(request):
    devices = models.Device.objects.all()
    context = {'devices': devices}
    return render(request, 'device_list.html', context)


#def device_detail(request, pk):
#    device = get_object_or_404(models.Device, pk=pk)
#    context = {'device': device}
#    return render(request, 'device_detail.html', context)

class DeviceDetailView(generic.DetailView):
    model = models.Device
    template_name = 'device_detail.html'
    context_object_name = 'device'


class DeviceCreateView(generic.CreateView):
    model = models.Device
    template_name = 'device_form.html'
    fields = ['name', 'serial_number']


class DeviceDeleteView(DeleteView):
    model = models.Device
    template_name = 'device_delete.html'
    success_url = reverse_lazy('device_list')

