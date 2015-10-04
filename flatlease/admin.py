from django.contrib import admin
from flatlease.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client


@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    model = FixedProperty
