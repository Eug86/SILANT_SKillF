from django.contrib import admin
from .models import Client, Company, Machine, TO, Claim, Buyer


@admin.register(Client)
class AnnAdmin(admin.ModelAdmin):
    model = Client


@admin.register(Buyer)
class AnnAdmin(admin.ModelAdmin):
    model = Buyer


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
