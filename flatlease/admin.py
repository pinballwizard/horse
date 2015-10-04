from django.contrib import admin
from flatlease.models import *


@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    list_display = ('location', 'cost', 'owner')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'second_name', 'birthday', 'residence', 'phone', 'deposit')
