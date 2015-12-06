from django.contrib import admin
from flatlease.models import *

admin.AdminSite.site_header = "Администрирование ЖиЛизинг"
admin.AdminSite.site_title = "Хорс-инвест"
admin.AdminSite.index_title = "ЖиЛизинг"


@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    search_fields = ['location', 'owner']
    list_display = ('location', 'cost', 'owner')


class FixedPropertyInLine(admin.TabularInline):
    model = FixedProperty
    extra = 1



