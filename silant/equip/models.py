from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Companies'


class TypeMachine(models.Model):
    name = models.CharField(max_length=8)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class TypeMotor(models.Model):
    name = models.CharField(max_length=16);
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class TypeTranc(models.Model):
    name = models.CharField(max_length=16);
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class TypeVmost(models.Model):
    name = models.CharField(max_length=16);
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class TypeCmost(models.Model):
    name = models.CharField(max_length=16);
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Machine(models.Model):
    n_machine = models.CharField(max_length=32)
    type_machine = models.ForeignKey(TypeMachine, on_delete=models.CASCADE, related_name='machines_typemachine')
    n_motor = models.CharField(max_length=32)
    type_motor = models.ForeignKey(TypeMotor, on_delete=models.CASCADE, related_name='machines_typemotor')
    n_tranc = models.CharField(max_length=32)
    type_tranc = models.ForeignKey(TypeTranc, on_delete=models.CASCADE, related_name='machines_typetranc')
    n_vmost = models.CharField(max_length=32)
    type_vmost = models.ForeignKey(TypeVmost, on_delete=models.CASCADE, related_name='machines_typevmost')
    n_cmost = models.CharField(max_length=32)
    type_cmost = models.ForeignKey(TypeCmost, on_delete=models.CASCADE, related_name='machines_typecmost')
    order = models.CharField(max_length=16)
    date = models.DateField()
    buyer = models.CharField(max_length=32)
    address = models.TextField()
    options = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='machines_client')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='machines_service')

    def __str__(self):
        return f'{self.n_machine}: {self.type_machine}'


class TO(models.Model):
    TYPE_TO = (
        ('TO-0', 'ТО-0 (50 м/час)'),
        ('TO-1', 'ТО-1 (200 м/час)'),
        ('TO-2', 'ТО-2 (400 м/час)'),
        ('TO-4', 'ТО-4 (1000м/час)'),
        ('TO-5', 'ТО-5 (2000м/час)')
    )

    type_to = models.CharField(max_length=12, choices=TYPE_TO, default='TO-0')
    date = models.DateField()
    narabotka = models.CharField(max_length=8)
    order = models.CharField(max_length=16)
    date_order = models.DateField()
    doTOservice = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='service_do_tos')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine_tos')


    def __str__(self):
        return f'{self.type_to}: {self.machine} ---- {self.order}'


class Claim(models.Model):
    date = models.DateField()
    narabotka = models.CharField(max_length=8)
    detail = models.CharField(max_length=32)
    info = models.TextField()
    fix = models.TextField()
    fix_detail = models.TextField()
    fix_date = models.DateField()
    stop_date = models.CharField(max_length=8)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine_claims')
    service = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='service_claims')

    def __str__(self):
        return f'{self.date}: {self.machine} - {self.detail}'

