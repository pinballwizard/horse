from django.contrib import admin
from flatlease.models import *


@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    list_display = ('location', 'cost', 'owner')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('count', 'pay_type', 'pay_date', 'owner')


@admin.register(Documents)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'owner', 'pub_date')


class DocumentsInLine(admin.StackedInline):
    model = Documents
    extra = 1


class FixedPropertyInLine(admin.StackedInline):
    model = FixedProperty
    extra = 1


class TransactionInLine(admin.StackedInline):
    model = Transaction
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'second_name', 'birthday', 'residence', 'phone', 'deposit', 'pub_date')
    inlines = [
        TransactionInLine,
        FixedPropertyInLine,
        DocumentsInLine,
    ]
