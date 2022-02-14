from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Vehicle
from django.urls import reverse_lazy


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'


class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ('name', 'model', 'make', 'Client', 'VIN', 'Date_of_Purchase', 'Date_of_LastService')
    template_name = 'vehicle_edit.html'


class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('name', 'model', 'make', 'Client', 'VIN', 'Date_of_Purchase', 'Date_of_LastService')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
