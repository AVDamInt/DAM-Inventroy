from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from . import forms
from .forms import UploadFileForm
from . import utils
from . import filters
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin


# def index(request):
#    return HttpResponse("Warehouse!")

# def device_list(request):
#    paginate_by = 10
#    devices = models.Device.objects.all()
#    context = {'devices': devices}
#    return render(request, 'device_list.html', context)


def device_list(request):
    devices = models.Device.objects.all()

    myFilter = filters.DeviceFilter(request.GET, queryset=devices)
    devices = myFilter.qs

    context = {'devices': devices, 'myFilter': myFilter}
    return render(request, 'device_list.html', context)


class DeviceListView(generic.ListView):
    paginate_by = 10
    model = models.Device
    template_name = 'device_list.html'
    devices = models.Device.objects.all()
    #device_count = devices.count()
    #context = {'devices': devices, 'device_count': device_count}
    # context_object_name = 'devices'

# LoginRequiredMixin
class DeviceList(FilterView):
    # login_url = 'accounts/login'
    # redirect_field_name = 'redirect_to'
    paginate_by = 10

    model = models.Device
    context_object_name = 'devices'
    template_name = 'device_list.html'
    filterset_class = filters.DeviceFilter


# def device_detail(request, pk):
#    device = get_object_or_404(models.Device, pk=pk)
#    context = {'device': device}
#    return render(request, 'device_detail.html', context)

#LoginRequiredMixin,
class DeviceDetailView(generic.DetailView):
    # login_url = 'accounts/login'
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

#@login_required(login_url='/accounts/login/')
def create_device(request):
    if request.method == 'POST':
        instance_form = forms.DeviceForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('device_list'))
    else:
        form = forms.DeviceForm()
        return render(request, 'device_form.html', {'form': form})

# LoginRequiredMixin,
class DeviceDeleteView(DeleteView):
    # login_url = 'accounts/login'
    model = models.Device
    template_name = 'device_delete.html'
    success_url = reverse_lazy('device_list')


class PlaceListView(generic.ListView):
    paginate_by = 10
    model = models.Place
    template_name = 'place_list.html'
    context_object_name = 'places'

# LoginRequiredMixin,
class PlaceList(FilterView):
    # login_url = 'accounts/login'
    paginate_by = 10
    model = models.Place
    context_object_name = 'places'
    template_name = 'place_list.html'
    filterset_class = filters.PlaceFilter


# def place_list(request):
#    places = models.Place.objects.all()
#    context = {'places': places}
#    return render(request, 'place_list.html', context)

# LoginRequiredMixin,
class PlaceCreateView(generic.CreateView):
    # login_url = 'accounts/login'
    model = models.Place
    template_name = 'place_form.html'
    fields = fields = '__all__'

# LoginRequiredMixin,
class PlaceDeleteView(DeleteView):
    # login_url = 'accounts/login'
    model = models.Place
    template_name = 'place_delete.html'
    success_url = reverse_lazy('place_list')

# LoginRequiredMixin,
class PlaceDetailView(generic.DetailView):
    # login_url = 'accounts/login'
    model = models.Place
    template_name = 'place_detail.html'
    context_object_name = 'place'


# class UserListView(generic.ListView):
#    paginate_by = 10
#    model = models.DeviceUser
#    template_name = 'user_list.html'
#    context_object_name = 'users'

#LoginRequiredMixin,
class UserListView(generic.ListView):
    # login_url = 'accounts/login'
    paginate_by = 10
    model = models.DeviceUser
    template_name = 'user_list.html'
    context_object_name = 'users'

#LoginRequiredMixin,
class UserList(FilterView):
    # login_url = 'accounts/login'
    paginate_by = 10
    model = models.DeviceUser
    context_object_name = 'users'
    template_name = 'user_list.html'
    filterset_class = filters.DeviceUserFilter

# LoginRequiredMixin,
class UserCreateView(generic.CreateView):
    # login_url = 'accounts/login'
    model = models.DeviceUser
    template_name = 'user_form.html'
    fields = '__all__'

    success_url = reverse_lazy('user_list')


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    # login_url = 'accounts/login'
    model = models.DeviceUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')


@login_required(login_url='/accounts/login/')
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            utils.handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse_lazy('device_list'))
        else:
            form = UploadFileForm()
            return render(request, 'file_upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'file_upload.html', {'form': form})
