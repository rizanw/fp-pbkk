from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import APD, Hospital, Transaction, TransactionDetail


class TransactionDetailAdmin(StackedInline):
    model = TransactionDetail


@register(APD)
class ApdAdmin(ModelAdmin):
    list_display = ('name', 'detail')


@register(Hospital)
class HospitalAdmin(ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('verified',)


@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('hospital', 'date_created')
    list_filter = ('type',)
    readonly_fields = ('date_created',)
    inlines = (TransactionDetailAdmin,)
