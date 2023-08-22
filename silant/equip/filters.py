from django_filters import FilterSet, CharFilter
from .models import Machine, TO, Claim


class MachineFilter(FilterSet):
    n_machine = CharFilter(field_name='n_machine', label='Заводской № машины')

    class Meta:
        model = Machine
        fields = {
            'n_machine'
        }


class MachineDetailFilter(FilterSet):
    n_machine = CharFilter(field_name='n_machine', label='Заводской № машины')

    class Meta:
        model = Machine
        fields = {
            'n_machine',
            'type_machine',
            'type_motor',
            'type_tranc',
            'type_vmost',
            'type_cmost',
        }


class TOFilter(FilterSet):
    type_to = CharFilter(field_name='type_to', label='Тип ТО')
    machine = CharFilter(field_name='machine', label='Машина')
    doTOservice = CharFilter(field_name='doTOservice', label='Сервис, выполнивший ТО')

    class Meta:
        model = TO
        fields = {
            'type_to',
            'machine',
            'doTOservice',
        }


class ClaimFilter(FilterSet):
    detail = CharFilter(field_name='detail', label='Узел')
    fix = CharFilter(field_name='fix', label='Способ восстановления')
    service = CharFilter(field_name='service', label='Сервис, выполнивший работы')

    class Meta:
        model = Claim
        fields = {
            'detail',
            'fix',
            'service',
        }