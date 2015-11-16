from django.contrib import admin
from flatlease.models import *

admin.AdminSite.site_header = "Администрирование ЖиЛизинг"
admin.AdminSite.site_title = "Хорс-инвест"
admin.AdminSite.index_title = "ЖиЛизинг"

@admin.register(FixedProperty)
class FixedPropertyAdmin(admin.ModelAdmin):
    search_fields = ['location', 'owner']
    list_display = ('location', 'cost', 'owner')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['pub_date', 'owner']
    readonly_fields = ('pub_date',)
    list_display = ('pub_date', 'count', 'type', 'owner')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['pub_date', 'owner']
    readonly_fields = ('pub_date',)
    list_display = ('type', 'owner', 'pub_date')


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    search_fields = ['number', 'owner']
    list_display = ('number', 'owner')


class DocumentInLine(admin.TabularInline):
    readonly_fields = ('pub_date',)
    model = Document
    extra = 1


class FixedPropertyInLine(admin.TabularInline):
    model = FixedProperty
    extra = 1


class PassportInLine(admin.StackedInline):
    model = Passport
    extra = 1


class RelativeInLine(admin.StackedInline):
    model = Relative
    extra = 1


class SpouseInLine(admin.StackedInline):
    model = Spouse


class TransactionInLine(admin.TabularInline):
    model = Transaction
    extra = 1
    readonly_fields = ('pub_date',)
    fields = (
        ('type', 'count', 'pub_date'),
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['last_name', 'name', 'phone']
    readonly_fields = ('id','pub_date','monthly_payment','balance','debt')
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
        DocumentInLine,
        PassportInLine,
        RelativeInLine,
        SpouseInLine,
    ]
