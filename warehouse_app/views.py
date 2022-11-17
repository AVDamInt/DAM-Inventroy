from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from . import forms
from django.contrib.auth.models import User

# def index(request):
#    return HttpResponse("Warehouse!")

def device_list(request):
    devices = models.Device.objects.all()
    context = {'devices': devices}
    return render(request, 'device_list.html', context)


# class DeviceListView(generic.ListView):
#    model = models.Device
#    template_name = 'device_list.html'
#    context_object_name = 'device'   


# def device_detail(request, pk):
#    device = get_object_or_404(models.Device, pk=pk)
#    context = {'device': device}
#    return render(request, 'device_detail.html', context)

class DeviceDetailView(generic.DetailView):
    model = models.Device
    template_name = 'device_detail.html'
    context_object_name = 'device'


# class DeviceCreateView(generic.CreateView):
#   model = models.Device
#   template_name = 'device_form.html'
#   fields = [
#       'name',
#       'serial_number',
#       'contract',
#       'expiration_date',
#       'renewal_date',
#       'host_name',
#       'make',
#       'model',
#       'place'
#       ]

# class DeviceCreateView(generic.CreateView):
#    model = models.Device
#    form_class = DeviceForm
#    template_name = 'device_form.html'
#    fields = [
#        'name',
#        'serial_number',
#        'contract',
#        'expiration_date',
#        'renewal_date',
#        'host_name',
#        'make',
#        'model',
#        'place'
#        ]

def create_device(request):
    if request.method == 'POST':
        instance_form = forms.DeviceForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('device_list'))
    else:
        form = forms.DeviceForm()
        return render(request, 'device_form.html', {'form': form})


class DeviceDeleteView(DeleteView):
    model = models.Device
    template_name = 'device_delete.html'
    success_url = reverse_lazy('device_list')


class PlaceListView(generic.ListView):
    model = models.Place
    template_name = 'place_list.html'
    context_object_name = 'place'


def place_list(request):
    places = models.Place.objects.all()
    context = {'places': places}
    return render(request, 'place_list.html', context)


class PlaceCreateView(generic.CreateView):
    model = models.Place
    template_name = 'place_form.html'
    fields = [
        'name',
        'city',
        'address',
        'cap',
        'country',
        'plan'
    ]


class PlaceDeleteView(DeleteView):
    model = models.Place
    template_name = 'place_delete.html'
    success_url = reverse_lazy('place_list')


class PlaceDetailView(generic.DetailView):
    model = models.Place
    template_name = 'place_detail.html'
    context_object_name = 'place'


class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'