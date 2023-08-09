from django.views.generic import ListView, DetailView
from .models import Machine, Client, Company, TO, Claim
from .filters import MachineFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect


class UnauthorizedList(ListView):
    model = Machine
    ordering = 'date'
    template_name = 'unauthorized.html'
    context_object_name = 'machines'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


@method_decorator(login_required, name='dispatch')
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
        user = self.request.user
        user_in_group_managers = user.groups.filter(name='managers').exists()
        user_in_group_clients = user.groups.filter(name='clients').exists()
        user_in_group_service = user.groups.filter(name='service').exists()
        context['user_in_group_managers'] = user_in_group_managers
        context['user_in_group_clients'] = user_in_group_clients
        context['user_in_group_service'] = user_in_group_service
        if user_in_group_clients:
            client = Client.objects.get(name=user)
            context['clients_machines'] = Machine.objects.filter(client=client).order_by('-date')
            print(client)
        elif user_in_group_service:
            company = Company.objects.get(name=user)
            context['service_machines'] = Machine.objects.filter(company=company).order_by('-date')
            print(company)
        return context


def MachineDetail(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    tos = machine.machine_tos.order_by('-date')
    claims = machine.machine_claims.order_by('-date')
    return render(request, 'machine.html', {'machine': machine, 'tos': tos, 'claims': claims})


class TOList(ListView):
    model = TO
    template_name = 'machine.html'
    context_object_name = 'tos'


class ClaimList(ListView):
    model = Claim
    template_name = 'claim.html'
    context_object_name = 'claims'