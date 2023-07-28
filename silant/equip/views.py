from django.views.generic import ListView
from .models import Machine
from .filters import MachineFilter


class MachineList(ListView):
    model = Machine
    ordering = 'date'
    template_name = 'main.html'
    context_object_name = 'machines'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
