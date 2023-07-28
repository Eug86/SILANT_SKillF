from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


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


class Machine(models.Model):
    TYPE_MA = (
        ('PD1,5', 'ПД1,5'),
        ('PG1,5', 'ПГ1,5'),
        ('PD2,0', 'ПД2,0'),
        ('PD2,5', 'ПД2,5'),
        ('PD3,0', 'ПД3,0'),
        ('PD5,0', 'ПД5,0')
    )
    TYPE_MO = (
        ('D1803', 'Kubota D1803'),
        ('D-243', 'ММЗ Д-243'),
        ('V3300', 'Kubota V3300'),
        ('K21', 'Nissan K21'),
        ('MMZ-4D', 'MMZ-4D')
    )
    TYPE_T = (
        ('HF30', 'HF30-VP010'),
        ('HF50', 'HF50-VP020'),
        ('10VA', '10VA-00105'),
        ('10VB', '10VB-00106')
    )
    TYPE_VM = (
        ('20VA', '20VA-00101'),
        ('20VB', '20VB-00102'),
        ('HA50', 'HA50-VP010'),
        ('HA30', 'HA30-02020')
    )
    TYPE_CM = (
        ('B35', 'B350655A'),
        ('VS30', 'VS30-00001'),
        ('VS20', 'VS20-00001')
    )

    n_machine = models.CharField(max_length=32)
    type_machine = models.CharField(max_length=12, choices=TYPE_MA, default='PD1,5')
    n_motor = models.CharField(max_length=32)
    type_motor = models.CharField(max_length=16, choices=TYPE_MO, default='D1803')
    n_tranc = models.CharField(max_length=32)
    type_tranc = models.CharField(max_length=16, choices=TYPE_T, default='HF30')
    n_vmost = models.CharField(max_length=32)
    type_vmost = models.CharField(max_length=16, choices=TYPE_VM, default='20VA')
    n_cmost = models.CharField(max_length=32)
    type_cmost = models.CharField(max_length=16, choices=TYPE_CM, default='B35')
    order = models.CharField(max_length=16)
    date = models.DateField()
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)
    address = models.TextField()
    options = models.TextField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='service_machines')

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
    service = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='service_tos')

    def __str__(self):
        return f'{self.type_to}: {self.machine}'


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

