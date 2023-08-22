from django import forms
from .models import Machine, TO, Claim, TypeMachine, TypeMotor, TypeTranc, TypeVmost, TypeCmost


class TypeMachineForm(forms.ModelForm):

    class Meta:
        model = TypeMachine
        fields = [
            'name',
            'description'
        ]


class TypeMotorForm(forms.ModelForm):

    class Meta:
        model = TypeMotor
        fields = [
            'name',
            'description'
        ]


class TypeTrancForm(forms.ModelForm):

    class Meta:
        model = TypeTranc
        fields = [
            'name',
            'description'
        ]


class TypeVmostForm(forms.ModelForm):

    class Meta:
        model = TypeVmost
        fields = [
            'name',
            'description'
        ]


class TypeCmostForm(forms.ModelForm):

    class Meta:
        model = TypeCmost
        fields = [
            'name',
            'description'
        ]


class MachineForm(forms.ModelForm):

    class Meta:
        model = Machine
        fields = [
            'n_machine',
            'type_machine',
            'n_motor',
            'type_motor',
            'n_tranc',
            'type_tranc',
            'n_vmost',
            'type_vmost',
            'n_cmost',
            'type_cmost',
            'order',
            'date',
            'buyer',
            'address',
            'options',
            'client',
            'company'
        ]


class TOForm(forms.ModelForm):

    class Meta:
        model = TO
        fields = [
            'type_to',
            'date',
            'narabotka',
            'order',
            'date_order',
            'doTOservice',
            'machine',
        ]


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = [
            'date',
            'narabotka',
            'detail',
            'info',
            'fix',
            'fix_detail',
            'fix_date',
            'stop_date',
            'machine',
            'service'
        ]