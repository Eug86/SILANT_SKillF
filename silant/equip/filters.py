from django_filters import FilterSet, CharFilter
from django.core.exceptions import ValidationError
from .models import Machine


class MachineFilter(FilterSet):
    n_machine = CharFilter(field_name='n_machine', label='Заводской № машины')

    class Meta:
        model = Machine
        fields = {
            'n_machine'
        }


