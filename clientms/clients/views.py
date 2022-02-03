from django.views.generic import ListView
from .models import models
from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
