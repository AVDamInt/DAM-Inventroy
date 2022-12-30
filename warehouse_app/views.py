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
from django.views.generic.edit import UpdateView


@login_required(login_url='/accounts/login/')
def create_device(request):
    if request.method == 'POST':
        instance_form = forms.DeviceForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('device_list'))
    else:
        form = forms.DeviceForm()
        return render(request, 'device_form.html', {'form': form})


class DeviceList(LoginRequiredMixin, FilterView):
    # login_url = 'accounts/login'
    # redirect_field_name = 'redirect_to'
    paginate_by = 10
    context_object_name = 'devices'
    model = models.Device
    template_name = 'device_list.html'
    filterset_class = filters.DeviceFilter

    def get_context_data(self, **kwargs):
        context = super(DeviceList, self).get_context_data(**kwargs)
        context['hist_devices'] = (models.Device.objects.filter(status=1)).count()
        context['active_devices'] = (models.Device.objects.filter(status=0)).count()
        context['available_devices'] = (models.Device.objects.filter(status=2)).count()
        return context


class DeviceDetailView(LoginRequiredMixin, generic.DetailView):
    # login_url = 'accounts/login'
    model = models.Device
    template_name = 'device_detail.html'
    context_object_name = 'device'


@login_required(login_url='/accounts/login/')
def update_device(request):
    print("HI")
    if request.method == 'POST':
        instance_form = forms.DeviceUpdateForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('device_list'))
    else:
        form = forms.DeviceUpdateForm()
    return render(request, 'device_update_form.html', {'form': form})


class DeviceUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "device_update_form.html"
    model = models.Device
    form_class = forms.DeviceUpdateForm


@login_required(login_url='/accounts/login/')
def delete_device(request, id):
    context = {}

    obj = get_object_or_404(models.Device, id=id)

    if request.method == 'POST':
        obj.status = models.Device.status_bol = 1
        # obj.status = models.Device.status_bol = False
        obj.save()
        return HttpResponseRedirect('/')
    return render(request, 'device_delete.html', context)


@login_required(login_url='/accounts/login/')
def create_place(request):
    if request.method == 'POST':
        instance_form = forms.PlaceForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('place_list'))
    else:
        form = forms.PlaceForm()
        return render(request, 'place_form.html', {'form': form})


class PlaceList(LoginRequiredMixin, FilterView):
    # login_url = 'accounts/login'
    paginate_by = 10
    model = models.Place
    context_object_name = 'places'
    template_name = 'place_list.html'
    filterset_class = filters.PlaceFilter


class PlaceDetailView(LoginRequiredMixin, generic.DetailView):
    # login_url = 'accounts/login'
    model = models.Place
    template_name = 'place_detail.html'
    context_object_name = 'place'


class PlaceUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "place_update_form.html"
    model = models.Place
    form_class = forms.PlaceUpdateForm


class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = 'accounts/login'
    model = models.Place
    template_name = 'place_delete.html'
    success_url = reverse_lazy('place_list')


@login_required(login_url='/accounts/login/')
def create_user_device(request):
    if request.method == 'POST':
        instance_form = forms.DeviceUserForm(request.POST)
        if instance_form.is_valid():
            instance_form.save()
            return HttpResponseRedirect(reverse_lazy('user_list'))
    else:
        form = forms.DeviceUserForm()
        return render(request, 'user_form.html', {'form': form})


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    # login_url = 'accounts/login'
    model = models.DeviceUser
    template_name = 'user_form.html'
    fields = '__all__'

    success_url = reverse_lazy('user_list')


class UserList(LoginRequiredMixin, FilterView):
    # login_url = 'accounts/login'
    paginate_by = 10
    model = models.DeviceUser
    context_object_name = 'users'
    template_name = 'user_list.html'
    filterset_class = filters.DeviceUserFilter


class DeviceUserDetailView(LoginRequiredMixin, generic.DetailView):
    # login_url = 'accounts/login'
    model = models.DeviceUser
    template_name = 'user_detail.html'
    context_object_name = 'deviceuser'


class DeviceUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "user_update_form.html"
    model = models.DeviceUser
    form_class = forms.DeviceUserUpdateForm


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
