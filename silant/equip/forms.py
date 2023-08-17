from django import forms
from .models import Machine, Client, Company, TO, Claim, TypeMachine, TypeMotor, TypeTranc, TypeVmost, TypeCmost


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