from django.contrib import admin
from flatlease.models import *
from car_leasing.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ['model', 'owner']
    list_display = ('model', 'owner', 'man_date', 'color', 'mileage')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'name', 'year']
    list_display = ('brand', 'name', 'year')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'logo')


