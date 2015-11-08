from django.contrib import admin
from flatlease.models import *


@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    list_display = ('location', 'cost', 'owner')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('pub_date', 'count', 'type', 'owner')


@admin.register(Document)
class DocumentsAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('type', 'owner', 'pub_date')


class DocumentsInLine(admin.TabularInline):
    readonly_fields = ('pub_date',)
    model = Document
    extra = 1


class FixedPropertyInLine(admin.TabularInline):
    model = FixedProperty
    extra = 1


class TransactionInLine(admin.TabularInline):
    model = Transaction
    extra = 1
    readonly_fields = ('pub_date',)
    fields = (
        ('type', 'count', 'pub_date'),
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date','monthly_payment','balance','debt')
    # fields = (
    #     ('pub_date', 'monthly_payment', 'balance', 'debt'),
    #     ('last_name', 'name', 'second_name'),
    #     'birthday',
    #     'residence',
    #     ('phone', 'email'),
    #     ('photo', 'passport'),
    #     'comment'
    # )
    list_display = ('last_name', 'name', 'second_name', 'birthday', 'residence', 'phone', 'balance', 'pub_date')
    inlines = [
        TransactionInLine,
        FixedPropertyInLine,
        DocumentsInLine,
    ]
