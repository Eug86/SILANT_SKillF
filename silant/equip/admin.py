from django.contrib import admin
from .models import Client, Company, Machine, TO, Claim


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
