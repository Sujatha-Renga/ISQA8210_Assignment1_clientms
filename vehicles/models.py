from django.db import models
from clients.models import Client
from django.urls import reverse


class Vehicle(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=80)
    Client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='vehicle',
    )
    VIN = models.CharField(max_length=20)
    Date_of_Purchase = models.DateField(auto_now_add=False)
    Date_of_LastService = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])
