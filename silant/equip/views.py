from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Machine, Client, Company, TO, Claim, TypeMachine, TypeMotor, TypeTranc, TypeVmost, TypeCmost
from .filters import MachineFilter
from .forms import TypeMachineForm, TypeMotorForm, TypeTrancForm, TypeVmostForm, TypeCmostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


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
    template_name = 'tos.html'
    context_object_name = 'tos'


class ClaimList(ListView):
    model = Claim
    template_name = 'claim.html'
    context_object_name = 'claims'


@method_decorator(login_required, name='dispatch')
class CreateTypeMachine(PermissionRequiredMixin, CreateView):
    permission_required = ('equip.add_typemachine',)
    form_class = TypeMachineForm
    model = TypeMachine
    template_name = 'edit_type_machine.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class EditTypeMachine(PermissionRequiredMixin, UpdateView):
    permission_required = ('equip.add_typemachine',)
    form_class = TypeMachineForm
    model = TypeMachine
    template_name = 'edit_type_machine.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class DeleteTypeMachine(PermissionRequiredMixin, DeleteView):
    permission_required = ('equip.delete_typemachine',)
    model = TypeMachine
    template_name = 'delete_type_machine.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class CreateTypeMotor(PermissionRequiredMixin, CreateView):
    permission_required = ('equip.add_typemotor',)
    form_class = TypeMotorForm
    model = TypeMotor
    template_name = 'edit_type_motor.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class EditTypeMotor(PermissionRequiredMixin, UpdateView):
    permission_required = ('equip.add_typemotor',)
    form_class = TypeMotorForm
    model = TypeMotor
    template_name = 'edit_type_motor.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class DeleteTypeMotor(PermissionRequiredMixin, DeleteView):
    permission_required = ('equip.delete_typemotor',)
    model = TypeMotor
    template_name = 'delete_type_motor.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class CreateTypeTranc(PermissionRequiredMixin, CreateView):
    permission_required = ('equip.add_typetranc',)
    form_class = TypeTrancForm
    model = TypeTranc
    template_name = 'edit_type_tranc.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class EditTypeTranc(PermissionRequiredMixin, UpdateView):
    permission_required = ('equip.add_typetranc',)
    form_class = TypeTrancForm
    model = TypeTranc
    template_name = 'edit_type_tranc.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class DeleteTypeTranc(PermissionRequiredMixin, DeleteView):
    permission_required = ('equip.delete_typetranc',)
    model = TypeTranc
    template_name = 'delete_type_tranc.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class CreateTypeVmost(PermissionRequiredMixin, CreateView):
    permission_required = ('equip.add_typevmost',)
    form_class = TypeVmostForm
    model = TypeVmost
    template_name = 'edit_type_vmost.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class EditTypeVmost(PermissionRequiredMixin, UpdateView):
    permission_required = ('equip.add_typevmost',)
    form_class = TypeVmostForm
    model = TypeVmost
    template_name = 'edit_type_vmost.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class DeleteTypeVmost(PermissionRequiredMixin, DeleteView):
    permission_required = ('equip.delete_typevmost',)
    model = TypeVmost
    template_name = 'delete_type_vmost.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class CreateTypeCmost(PermissionRequiredMixin, CreateView):
    permission_required = ('equip.add_typecmost',)
    form_class = TypeCmostForm
    model = TypeCmost
    template_name = 'edit_type_cmost.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class EditTypeCmost(PermissionRequiredMixin, UpdateView):
    permission_required = ('equip.add_typecmost',)
    form_class = TypeCmostForm
    model = TypeCmost
    template_name = 'edit_type_cmost.html'
    success_url = reverse_lazy('list')


@method_decorator(login_required, name='dispatch')
class DeleteTypeCmost(PermissionRequiredMixin, DeleteView):
    permission_required = ('equip.delete_typecmost',)
    model = TypeCmost
    template_name = 'delete_type_cmost.html'
    success_url = reverse_lazy('list')


def List(request):
    typemachines = TypeMachine.objects.all()
    typemotors = TypeMotor.objects.all()
    typetrancs = TypeTranc.objects.all()
    typecmosts = TypeCmost.objects.all()
    typevmosts = TypeVmost.objects.all()
    return render(request, 'list.html', {'typemachines': typemachines, 'typemotors': typemotors, 'typetrancs': typetrancs, 'typevmosts': typevmosts, 'typecmosts': typecmosts})

def typemachine_detail(request, pk):
    typemachine = get_object_or_404(TypeMachine, pk=pk)
    return render(request, 'typemachine_detail.html', {'typemachine': typemachine})

def typemotor_detail(request, pk):
    typemotor = get_object_or_404(TypeMotor, pk=pk)
    return render(request, 'typemotor_detail.html', {'typemotor': typemotor})

def typetranc_detail(request, pk):
    typetranc = get_object_or_404(TypeTranc, pk=pk)
    return render(request, 'typetranc_detail.html', {'typetranc': typetranc})

def typecmost_detail(request, pk):
    typecmost = get_object_or_404(TypeCmost, pk=pk)
    return render(request, 'typecmost_detail.html', {'typecmost': typecmost})

def typevmost_detail(request, pk):
    typevmost = get_object_or_404(TypeVmost, pk=pk)
    return render(request, 'typevmost_detail.html', {'typevmost': typevmost})