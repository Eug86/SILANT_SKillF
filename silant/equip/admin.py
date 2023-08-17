from django.contrib import admin
from .models import Client, Company, Machine, TO, Claim, TypeMachine, TypeMotor, TypeTranc, TypeVmost, TypeCmost


@admin.register(Client)
class AnnAdmin(admin.ModelAdmin):
    model = Client


@admin.register(Company)
class AnnAdmin(admin.ModelAdmin):
    model = Company


@admin.register(Machine)
class AnnAdmin(admin.ModelAdmin):
    model = Machine


@admin.register(TO)
class AnnAdmin(admin.ModelAdmin):
    model = TO


@admin.register(Claim)
class AnnAdmin(admin.ModelAdmin):
    model = Claim


@admin.register(TypeMachine)
class AnnAdmin(admin.ModelAdmin):
    model = TypeMachine


@admin.register(TypeMotor)
class AnnAdmin(admin.ModelAdmin):
    model = TypeMotor


@admin.register(TypeTranc)
class AnnAdmin(admin.ModelAdmin):
    model = TypeTranc


@admin.register(TypeVmost)
class AnnAdmin(admin.ModelAdmin):
    model = TypeVmost


@admin.register(TypeCmost)
class AnnAdmin(admin.ModelAdmin):
    model = TypeCmost
