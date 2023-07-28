from django.views.generic import ListView
from .models import Machine


class MachineList(ListView):
    model = Machine
    ordering = 'date'
    template_name = 'main.html'
    context_object_name = 'machines'
